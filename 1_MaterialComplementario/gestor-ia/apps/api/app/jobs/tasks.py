from datetime import date

from app.db.session import SessionLocal
from app.db import models
from app.services.alerts import load_boe_changes, load_dehu_forwards
from app.services.ocr import extract_fields
from app.services.confidence import confidence_score
from app.core.security import encrypt_value


def process_boe_changes(user_id: int) -> int:
    session = SessionLocal()
    try:
        changes = load_boe_changes()
        count = 0
        for change in changes:
            alert = models.Alert(
                user_id=user_id,
                type="regulatory_change",
                title=change["title"],
                body=change["summary"],
                severity="warning",
            )
            session.add(alert)
            count += 1
        session.commit()
        return count
    finally:
        session.close()


def process_dehu_forward(user_id: int) -> int:
    session = SessionLocal()
    try:
        forwards = load_dehu_forwards()
        count = 0
        for forward in forwards:
            alert = models.Alert(
                user_id=user_id,
                type="dehu_notice",
                title=forward["title"],
                body=f"{forward['summary']} Borrador: {forward.get('draft_reply', '')}",
                severity="critical",
            )
            session.add(alert)
            count += 1
        session.commit()
        return count
    finally:
        session.close()


def process_ocr(user_id: int, filename: str) -> dict:
    payload = extract_fields(filename)
    score, checks = confidence_score(payload)
    payload["confidence"] = score
    payload["validation"] = checks
    if payload.get("nif"):
        payload["nif_encrypted"] = encrypt_value(payload["nif"])
        payload["nif_masked"] = payload["nif"][:2] + "***"
        payload["nif"] = ""
    if payload.get("cif"):
        payload["cif_encrypted"] = encrypt_value(payload["cif"])
        payload["cif_masked"] = payload["cif"][:2] + "***"
        payload["cif"] = ""

    session = SessionLocal()
    try:
        document = models.Document(
            user_id=user_id,
            type="receipt",
            filename=filename,
            storage_path=f"storage/{filename}",
            extracted_json=payload,
        )
        session.add(document)
        session.flush()
        vendor = payload.get("vendor") or "Proveedor detectado"
        vendor_lower = vendor.lower()
        category = "Por revisar"
        if "gasolinera" in vendor_lower:
            category = "Transporte"
        if "cowork" in vendor_lower:
            category = "Alquiler"
        if "iberdrola" in vendor_lower:
            category = "Suministros"

        expense = models.Expense(
            user_id=user_id,
            vendor=vendor,
            date=date.fromisoformat(payload.get("date") or "2025-01-01"),
            total=float(payload.get("total") or 0.0),
            vat=float(payload.get("vat") or 0.0),
            category=category,
            confidence=score,
            source_document_id=document.id,
        )
        session.add(expense)
        session.commit()
        return payload
    finally:
        session.close()


def process_whatsapp_event(user_id: int, text: str) -> dict:
    session = SessionLocal()
    try:
        event = models.WhatsappEvent(
            user_id=user_id,
            type="text",
            payload_json={"text": text, "channel": "whatsapp"},
        )
        session.add(event)

        # naive expense extraction from message text
        amount = 0.0
        for token in text.replace(",", ".").split():
            try:
                amount = float(token)
                break
            except ValueError:
                continue

        if amount > 0:
            expense = models.Expense(
                user_id=user_id,
                vendor="WhatsApp",
                date=date.today(),
                total=amount,
                vat=amount * 0.21,
                category="Por revisar",
                confidence=0.4,
            )
            session.add(expense)
            session.flush()
            session.add(
                models.AuditLog(
                    user_id=user_id,
                    action="create",
                    entity_type="expense",
                    entity_id=expense.id,
                    before_json=None,
                    after_json={"vendor": expense.vendor, "total": expense.total},
                )
            )

        session.commit()
        return {"status": "ok", "expense_created": amount > 0}
    finally:
        session.close()
