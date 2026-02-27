from datetime import date

from fastapi import APIRouter
from pydantic import BaseModel

from app.db.session import SessionLocal
from app.db import models
from app.api.utils import to_dict


router = APIRouter(prefix="/expenses", tags=["expenses"])


class ExpensePayload(BaseModel):
    user_id: int
    vendor: str
    date: str
    total: float
    vat: float | None = None
    category: str | None = None
    confidence: float | None = None
    source_document_id: int | None = None


@router.get("/")
def list_expenses(user_id: int):
    session = SessionLocal()
    try:
        items = session.query(models.Expense).filter_by(user_id=user_id).all()
        return [to_dict(item) for item in items]
    finally:
        session.close()


@router.post("/")
def create_expense(payload: ExpensePayload):
    session = SessionLocal()
    try:
        expense = models.Expense(
            user_id=payload.user_id,
            vendor=payload.vendor,
            date=date.fromisoformat(payload.date),
            total=payload.total,
            vat=payload.vat,
            category=payload.category,
            confidence=payload.confidence,
            source_document_id=payload.source_document_id,
        )
        session.add(expense)
        session.flush()
        session.add(
            models.AuditLog(
                user_id=payload.user_id,
                action="create",
                entity_type="expense",
                entity_id=expense.id,
                before_json=None,
                after_json={
                    "vendor": expense.vendor,
                    "total": expense.total,
                    "category": expense.category,
                },
            )
        )
        session.commit()
        return {"status": "ok", "id": expense.id}
    finally:
        session.close()
