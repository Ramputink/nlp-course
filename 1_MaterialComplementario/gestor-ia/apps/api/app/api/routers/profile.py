from datetime import date

from fastapi import APIRouter
from pydantic import BaseModel

from app.db.session import SessionLocal
from app.db import models
from app.api.utils import to_dict


router = APIRouter(prefix="/profile", tags=["profile"])


class ProfilePayload(BaseModel):
    provincia: str
    regimen_autonomo: str
    actividad: str
    start_date: str
    retention_days: int | None = None


@router.get("/{user_id}")
def get_profile(user_id: int):
    session = SessionLocal()
    try:
        profile = session.query(models.Profile).filter_by(user_id=user_id).first()
        return to_dict(profile) if profile else {}
    finally:
        session.close()


@router.post("/{user_id}")
def upsert_profile(user_id: int, payload: ProfilePayload):
    session = SessionLocal()
    try:
        profile = session.query(models.Profile).filter_by(user_id=user_id).first()
        if not profile:
            profile = models.Profile(user_id=user_id)
            session.add(profile)
        profile.provincia = payload.provincia
        profile.regimen_autonomo = payload.regimen_autonomo
        profile.actividad = payload.actividad
        profile.start_date = date.fromisoformat(payload.start_date)
        profile.retention_days = payload.retention_days
        session.commit()
        return {"status": "ok"}
    finally:
        session.close()
