import base64
import hashlib
from datetime import datetime, timedelta
from typing import Any, Dict

import jwt
from cryptography.fernet import Fernet, InvalidToken

from app.core.config import settings


def _derive_fernet_key(raw: str) -> bytes:
    digest = hashlib.sha256(raw.encode("utf-8")).digest()
    return base64.urlsafe_b64encode(digest)


def get_fernet() -> Fernet:
    try:
        key = settings.field_encryption_key.encode("utf-8")
        return Fernet(key)
    except Exception:
        return Fernet(_derive_fernet_key(settings.field_encryption_key))


def encrypt_value(value: str) -> str:
    if value is None:
        return ""
    token = get_fernet().encrypt(value.encode("utf-8"))
    return token.decode("utf-8")


def decrypt_value(value: str) -> str:
    if not value:
        return ""
    try:
        decrypted = get_fernet().decrypt(value.encode("utf-8"))
        return decrypted.decode("utf-8")
    except InvalidToken:
        return ""


def create_access_token(subject: str, extra: Dict[str, Any]) -> str:
    now = datetime.utcnow()
    payload = {
        "sub": subject,
        "iss": settings.jwt_issuer,
        "aud": settings.jwt_audience,
        "iat": now,
        "exp": now + timedelta(minutes=settings.jwt_expires_minutes),
        **extra,
    }
    return jwt.encode(payload, settings.secret_key, algorithm="HS256")


def decode_token(token: str) -> Dict[str, Any]:
    return jwt.decode(
        token,
        settings.secret_key,
        algorithms=["HS256"],
        audience=settings.jwt_audience,
        issuer=settings.jwt_issuer,
    )
