from fastapi import APIRouter
from pydantic import BaseModel

from app.db.session import SessionLocal
from app.db import models
from app.api.utils import to_dict


router = APIRouter(prefix="/filings", tags=["filings"])


class FilingPayload(BaseModel):
    user_id: int
    model: str
    period: str
    draft_json: dict


@router.get("/")
def list_filings(user_id: int):
    session = SessionLocal()
    try:
        items = session.query(models.Filing).filter_by(user_id=user_id).all()
        return [to_dict(item) for item in items]
    finally:
        session.close()


@router.post("/draft")
def create_draft(payload: FilingPayload):
    session = SessionLocal()
    try:
        filing = models.Filing(
            user_id=payload.user_id,
            model=payload.model,
            period=payload.period,
            draft_json=payload.draft_json,
            status="draft",
        )
        session.add(filing)
        session.commit()
        return {"status": "ok", "id": filing.id}
    finally:
        session.close()
