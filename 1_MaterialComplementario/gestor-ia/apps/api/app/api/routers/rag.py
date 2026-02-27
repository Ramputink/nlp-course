from fastapi import APIRouter
from pydantic import BaseModel

from app.core.config import settings
from app.db.session import SessionLocal
from app.db import models
from app.services.rag import answer_question


router = APIRouter(prefix="/rag", tags=["rag"])


class AskPayload(BaseModel):
    user_id: int
    question: str


class IngestPayload(BaseModel):
    refresh: bool = True


@router.post("/ask")
def ask(payload: AskPayload):
    session = SessionLocal()
    try:
        answer_text, citations, confidence = answer_question(
            session, payload.user_id, payload.question
        )
        answer = models.Answer(
            user_id=payload.user_id, question=payload.question, answer_text=answer_text
        )
        session.add(answer)
        session.flush()
        for cite in citations:
            session.add(
                models.Citation(
                    answer_id=answer.id,
                    source_id=cite["source_id"],
                    url=cite["url"],
                    snippet=cite["snippet"],
                    as_of_date=cite["as_of_date"],
                )
            )
        session.commit()
        needs_human = confidence < settings.rag_min_confidence
        return {
            "answer_id": answer.id,
            "answer_text": answer_text,
            "citations": citations,
            "confidence": confidence,
            "safety": {
                "needs_human": needs_human,
                "message": "Derivar a gestor y preparar audit pack."
                if needs_human
                else "Confianza suficiente para recomendacion.",
            },
        }
    finally:
        session.close()


@router.post("/ingest")
def ingest(payload: IngestPayload):
    from app.services.rag import load_fixture_sources, embed_text, ensure_gov_only
    from app.core.config import settings
    import os

    session = SessionLocal()
    try:
        sources = load_fixture_sources()
        ensure_gov_only(sources)
        for src in sources:
            raw_path = os.path.join(settings.storage_path, "sources", f"{src['id']}.txt")
            os.makedirs(os.path.dirname(raw_path), exist_ok=True)
            with open(raw_path, "w", encoding="utf-8") as fh:
                fh.write(src["raw_text"])
            embedding = embed_text(src["raw_text"])
            existing = session.query(models.Source).filter_by(id=src["id"]).first()
            if existing and payload.refresh:
                existing.title = src["title"]
                existing.url = src["url"]
                existing.content_hash = src["content_hash"]
                existing.raw_text_path = raw_path
                existing.embedding = embedding
            elif not existing:
                session.add(
                    models.Source(
                        id=src["id"],
                        jurisdiction=src["jurisdiction"],
                        agency=src["agency"],
                        title=src["title"],
                        url=src["url"],
                        content_hash=src["content_hash"],
                        raw_text_path=raw_path,
                        embedding=embedding,
                    )
                )
        session.commit()
        return {"status": "ok", "count": len(sources)}
    finally:
        session.close()
