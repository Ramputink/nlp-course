from fastapi import APIRouter
from pydantic import BaseModel
import redis
from rq import Queue

from app.core.config import settings
from app.db.session import SessionLocal
from app.db import models
from app.api.utils import to_dict
from app.jobs import tasks


router = APIRouter(prefix="/alerts", tags=["alerts"])


class TriggerPayload(BaseModel):
    user_id: int


@router.get("/")
def list_alerts(user_id: int):
    session = SessionLocal()
    try:
        items = session.query(models.Alert).filter_by(user_id=user_id).all()
        return [to_dict(item) for item in items]
    finally:
        session.close()


@router.post("/trigger/boe")
def trigger_boe(payload: TriggerPayload):
    redis_conn = redis.from_url(settings.redis_url)
    q = Queue("default", connection=redis_conn)
    job = q.enqueue(tasks.process_boe_changes, payload.user_id)
    return {"status": "queued", "job_id": job.id}


@router.post("/trigger/dehu")
def trigger_dehu(payload: TriggerPayload):
    redis_conn = redis.from_url(settings.redis_url)
    q = Queue("default", connection=redis_conn)
    job = q.enqueue(tasks.process_dehu_forward, payload.user_id)
    return {"status": "queued", "job_id": job.id}
