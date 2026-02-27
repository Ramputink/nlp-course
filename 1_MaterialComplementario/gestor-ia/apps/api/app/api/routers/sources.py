from fastapi import APIRouter

from app.db.session import SessionLocal
from app.db import models


router = APIRouter(prefix="/sources", tags=["sources"])


@router.get("/{source_id}")
def get_source(source_id: int, q: str = ""):
    session = SessionLocal()
    try:
        source = session.query(models.Source).filter_by(id=source_id).first()
        if not source:
            return {"error": "not_found"}
        with open(source.raw_text_path, "r", encoding="utf-8") as fh:
            raw_text = fh.read()
        snippet = raw_text[:400]
        highlighted = (
            snippet.replace(q, f"[[{q}]]") if q else snippet
        )
        return {
            "source_id": source.id,
            "title": source.title,
            "url": source.url,
            "snippet": snippet,
            "highlighted": highlighted,
        }
    finally:
        session.close()
