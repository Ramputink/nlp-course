from fastapi import APIRouter
from pydantic import BaseModel

from app.db.session import SessionLocal
from app.db import models
from app.api.utils import to_dict


router = APIRouter(prefix="/partners", tags=["partners"])


class ReviewRequest(BaseModel):
    filing_id: int
    partner_user_id: int


@router.get("/reviews")
def list_reviews(partner_user_id: int):
    session = SessionLocal()
    try:
        items = session.query(models.PartnerReview).filter_by(partner_user_id=partner_user_id).all()
        return [to_dict(item) for item in items]
    finally:
        session.close()


@router.post("/reviews/request")
def request_review(payload: ReviewRequest):
    session = SessionLocal()
    try:
        review = models.PartnerReview(
            filing_id=payload.filing_id,
            partner_user_id=payload.partner_user_id,
            status="pending",
            notes="Solicitud de revision",
        )
        session.add(review)
        session.commit()
        return {"status": "ok", "id": review.id}
    finally:
        session.close()


@router.post("/reviews/{review_id}/approve")
def approve_review(review_id: int):
    session = SessionLocal()
    try:
        review = session.query(models.PartnerReview).filter_by(id=review_id).first()
        if not review:
            return {"error": "not_found"}
        review.status = "approved"
        filing = session.query(models.Filing).filter_by(id=review.filing_id).first()
        if filing:
            filing.status = "ready"
        session.commit()
        return {"status": "approved"}
    finally:
        session.close()


@router.post("/reviews/{review_id}/reject")
def reject_review(review_id: int):
    session = SessionLocal()
    try:
        review = session.query(models.PartnerReview).filter_by(id=review_id).first()
        if not review:
            return {"error": "not_found"}
        review.status = "rejected"
        session.commit()
        return {"status": "rejected"}
    finally:
        session.close()
