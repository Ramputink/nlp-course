from fastapi import APIRouter

from app.db.session import SessionLocal
from app.db import models
from app.api.utils import to_dict


router = APIRouter(prefix="/data", tags=["data"])


@router.get("/export")
def export_data(user_id: int):
    session = SessionLocal()
    try:
        user = session.query(models.User).filter_by(id=user_id).first()
        profile = session.query(models.Profile).filter_by(user_id=user_id).first()
        expenses = session.query(models.Expense).filter_by(user_id=user_id).all()
        filings = session.query(models.Filing).filter_by(user_id=user_id).all()
        documents = session.query(models.Document).filter_by(user_id=user_id).all()
        return {
            "user": to_dict(user) if user else {},
            "profile": to_dict(profile) if profile else {},
            "expenses": [to_dict(e) for e in expenses],
            "filings": [to_dict(f) for f in filings],
            "documents": [to_dict(d) for d in documents],
        }
    finally:
        session.close()
