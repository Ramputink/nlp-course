from fastapi import APIRouter
from pydantic import BaseModel
import redis
from rq import Queue

from app.core.config import settings
from app.db.session import SessionLocal
from app.db import models
from app.api.utils import to_dict
from app.services.whatsapp import normalize_event, suggest_next_step
from app.jobs import tasks


router = APIRouter(prefix="/whatsapp", tags=["whatsapp"])


class WhatsappPayload(BaseModel):
    user_id: int
    type: str = "text"
    text: str | None = None


@router.get("/events")
def list_events(user_id: int):
    session = SessionLocal()
    try:
        items = (
            session.query(models.WhatsappEvent)
            .filter_by(user_id=user_id)
            .order_by(models.WhatsappEvent.created_at.desc())
            .limit(50)
            .all()
        )
        return [to_dict(item) for item in items]
    finally:
        session.close()


@router.post("/webhook")
def webhook(payload: WhatsappPayload):
    session = SessionLocal()
    try:
        event = normalize_event(payload.dict())
        row = models.WhatsappEvent(user_id=payload.user_id, type=event["type"], payload_json=event)
        session.add(row)
        session.commit()
        redis_conn = redis.from_url(settings.redis_url)
        q = Queue("default", connection=redis_conn)
        q.enqueue(tasks.process_whatsapp_event, payload.user_id, payload.text or "")
        return {"status": "ok", "next_step": suggest_next_step(event)}
    finally:
        session.close()


@router.post("/emulator")
def emulator(payload: WhatsappPayload):
    return webhook(payload)
