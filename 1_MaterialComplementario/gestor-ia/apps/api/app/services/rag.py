import hashlib
import json
import math
import os
from typing import Dict, List, Tuple

from sqlalchemy import select

from app.core.config import settings
from app.db import models


FIXTURES_PATH = os.path.join(os.path.dirname(__file__), "..", "fixtures")
GOV_AGENCIES = {"AEAT", "BOE", "DEHU"}


def load_fixture_sources() -> List[Dict]:
    with open(os.path.join(FIXTURES_PATH, "sources.json"), "r", encoding="utf-8") as fh:
        return json.load(fh)


def ensure_gov_only(sources: List[Dict]) -> None:
    for src in sources:
        if src["agency"] not in GOV_AGENCIES:
            raise ValueError(f"Non-gov source rejected: {src['agency']}")


def embed_text(text: str) -> List[float]:
    if not text:
        return [0.0] * 8
    digest = hashlib.sha256(text.encode("utf-8")).digest()
    vec = []
    for i in range(8):
        chunk = digest[i * 4 : (i + 1) * 4]
        value = int.from_bytes(chunk, "big") / 2**32
        vec.append(value)
    norm = math.sqrt(sum(v * v for v in vec)) or 1.0
    return [v / norm for v in vec]


def retrieve_sources(session, query: str, k: int = 3) -> List[models.Source]:
    qvec = embed_text(query)
    stmt = select(models.Source).order_by(models.Source.embedding.l2_distance(qvec)).limit(k)
    return list(session.execute(stmt).scalars())


def build_snippet(raw_text: str, query: str) -> str:
    lower = raw_text.lower()
    q = query.lower()
    idx = lower.find(q.split(" ")[0]) if q else -1
    if idx == -1:
        return raw_text[:220]
    start = max(idx - 40, 0)
    end = min(idx + 180, len(raw_text))
    return raw_text[start:end]


def answer_question(session, user_id: int, question: str) -> Tuple[str, List[Dict], float]:
    sources = retrieve_sources(session, question, k=3)
    fixture_map = {src["id"]: src for src in load_fixture_sources()}

    citations = []
    statements = []
    confidence = 0.0
    for idx, src in enumerate(sources, start=1):
        fixture = fixture_map.get(src.id)
        if not fixture:
            continue
        with open(src.raw_text_path, "r", encoding="utf-8") as fh:
            raw_text = fh.read()
        snippet = build_snippet(raw_text, question)
        citations.append(
            {
                "source_id": src.id,
                "url": src.url,
                "snippet": snippet,
                "as_of_date": fixture["as_of_date"],
            }
        )
        statements.append(
            f"{fixture['summary']} [{idx}]"
        )
        confidence = max(confidence, fixture.get("confidence", 0.6))

    if not statements:
        statements = ["No tengo suficiente informacion gubernamental para responder. [1]"]

    answer_text = " ".join(statements)
    return answer_text, citations, confidence
