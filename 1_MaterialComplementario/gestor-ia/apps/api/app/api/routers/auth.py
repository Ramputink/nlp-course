from fastapi import APIRouter
from pydantic import BaseModel

from app.core.security import create_access_token
from app.db.session import SessionLocal
from app.db import models


router = APIRouter(prefix="/auth", tags=["auth"])


class MagicLinkRequest(BaseModel):
    email: str


class VerifyRequest(BaseModel):
    email: str
    token: str


@router.post("/magic-link")
def magic_link(payload: MagicLinkRequest):
    token = f"mock-{payload.email}"
    return {
        "status": "sent",
        "token": token,
        "preview_url": f"http://localhost:3000/verify?token={token}&email={payload.email}",
    }


@router.post("/verify")
def verify(payload: VerifyRequest):
    session = SessionLocal()
    try:
        user = session.query(models.User).filter_by(email=payload.email).first()
        if not user:
            user = models.User(email=payload.email, role="user", locale="es-ES")
            session.add(user)
            session.commit()
        token = create_access_token(str(user.id), {"role": user.role})
        return {"access_token": token, "user_id": user.id, "role": user.role}
    finally:
        session.close()
