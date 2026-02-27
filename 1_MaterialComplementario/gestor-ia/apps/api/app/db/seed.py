import json
import os
from datetime import date, datetime

from sqlalchemy import select

from app.core.config import settings
from app.db.session import SessionLocal
from app.db import models
from app.services.rag import embed_text, ensure_gov_only
from app.core.security import encrypt_value


FIXTURES_PATH = os.path.join(os.path.dirname(__file__), "..", "fixtures")


def load_json(name: str):
    with open(os.path.join(FIXTURES_PATH, name), "r", encoding="utf-8") as fh:
        return json.load(fh)


def seed():
    session = SessionLocal()
    try:
        existing = session.execute(select(models.User)).first()
        if existing:
            print("Seed already applied.")
            return

        user = models.User(email="ana@autonomos.es", role="user", locale="es-ES")
        partner = models.User(email="gestor@partner.es", role="partner_gestor", locale="es-ES")
        session.add_all([user, partner])
        session.flush()

        profile = models.Profile(
            user_id=user.id,
            provincia="Madrid",
            regimen_autonomo="Estimacion directa",
            actividad="Consultoria",
            start_date=date(2021, 1, 1),
            retention_days=365,
        )
        session.add(profile)

        # Sources for RAG (gov-only)
        sources = load_json("sources.json")
        ensure_gov_only(sources)
        for src in sources:
            raw_path = os.path.join(settings.storage_path, "sources", f"{src['id']}.txt")
            os.makedirs(os.path.dirname(raw_path), exist_ok=True)
            with open(raw_path, "w", encoding="utf-8") as fh:
                fh.write(src["raw_text"])
            embedding = embed_text(src["raw_text"])
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

        # Documents + expenses
        doc = models.Document(
            user_id=user.id,
            type="receipt",
            filename="ticket_gasolina.pdf",
            storage_path="storage/docs/ticket_gasolina.pdf",
            extracted_json={
                "vendor": "Gasolinera Norte",
                "date": "2025-12-20",
                "total": 78.40,
                "vat": 13.60,
                "nif": "",
                "nif_masked": "B1***",
                "nif_encrypted": encrypt_value("B12345678"),
            },
        )
        session.add(doc)
        session.flush()

        expenses = [
            models.Expense(
                user_id=user.id,
                vendor="Gasolinera Norte",
                date=date(2025, 12, 20),
                total=78.40,
                vat=13.60,
                category="Transporte",
                confidence=0.82,
                source_document_id=doc.id,
            ),
            models.Expense(
                user_id=user.id,
                vendor="Cowork Central",
                date=date(2025, 12, 5),
                total=220.00,
                vat=38.20,
                category="Alquiler",
                confidence=0.9,
            ),
            models.Expense(
                user_id=user.id,
                vendor="Iberdrola",
                date=date(2025, 11, 28),
                total=95.30,
                vat=16.52,
                category="Suministros",
                confidence=0.77,
            ),
            models.Expense(
                user_id=user.id,
                vendor="Amazon Business",
                date=date(2025, 11, 18),
                total=49.99,
                vat=8.68,
                category="Material oficina",
                confidence=0.7,
            ),
        ]
        while len(expenses) < 10:
            idx = len(expenses) + 1
            expenses.append(
                models.Expense(
                    user_id=user.id,
                    vendor=f"Proveedor {idx}",
                    date=date(2025, 10, 1 + idx),
                    total=20.0 + idx,
                    vat=3.0 + idx / 10,
                    category="Otros",
                    confidence=0.6 + idx / 20,
                )
            )
        session.add_all(expenses)

        filings = [
            models.Filing(
                user_id=user.id,
                model="303",
                period="2025Q4",
                draft_json={"base": 12000, "vat": 2520},
                status="draft",
            ),
            models.Filing(
                user_id=user.id,
                model="130",
                period="2025Q4",
                draft_json={"base": 9000, "irpf": 1350},
                status="in_review",
            ),
        ]
        session.add_all(filings)
        session.flush()

        session.add(
            models.PartnerReview(
                filing_id=filings[1].id,
                partner_user_id=partner.id,
                status="pending",
                notes="Revisar gastos y retenciones.",
            )
        )

        alerts = [
            models.Alert(
                user_id=user.id,
                type="regulatory_change",
                title="Cambio en modelo 303",
                body="Se actualiza el resumen del modelo 303 para Q4.",
                severity="warning",
            ),
            models.Alert(
                user_id=user.id,
                type="dehu_notice",
                title="Notificacion DEHU: requerimiento",
                body="Recibida notificacion con plazo de 10 dias.",
                severity="critical",
            ),
            models.Alert(
                user_id=user.id,
                type="reminder",
                title="Checklist trimestral pendiente",
                body="Revisa tareas de Q4 antes del cierre.",
                severity="info",
            ),
        ]
        session.add_all(alerts)

        # WhatsApp events
        session.add_all(
            [
                models.WhatsappEvent(
                    user_id=user.id,
                    type="text",
                    payload_json={"text": "Gasto taxi 24 euros", "channel": "whatsapp"},
                ),
                models.WhatsappEvent(
                    user_id=user.id,
                    type="audio",
                    payload_json={"text": "Audio: factura coworking", "channel": "whatsapp"},
                ),
            ]
        )

        # Answer + citation sample
        answer = models.Answer(
            user_id=user.id,
            question="Puedo deducir gasolina?",
            answer_text="Si el gasto esta vinculado a la actividad, puedes deducirlo con la documentacion adecuada. [1]",
        )
        session.add(answer)
        session.flush()
        session.add(
            models.Citation(
                answer_id=answer.id,
                source_id=1,
                url="https://www.agenciatributaria.es",
                snippet="Los gastos vinculados a la actividad economica pueden ser deducibles si estan justificados.",
                as_of_date="2025-12-15",
            )
        )

        session.add(
            models.AuditLog(
                user_id=user.id,
                action="seed",
                entity_type="system",
                entity_id=None,
                before_json=None,
                after_json={"status": "seed_complete", "ts": datetime.utcnow().isoformat()},
            )
        )

        session.commit()
        print("Seed complete.")
    finally:
        session.close()


if __name__ == "__main__":
    seed()
