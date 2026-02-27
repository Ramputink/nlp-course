from typing import Dict


def normalize_event(payload: Dict) -> Dict:
    event_type = payload.get("type", "text")
    text = payload.get("text", "")
    return {
        "type": event_type,
        "text": text,
        "channel": "whatsapp",
    }


def suggest_next_step(event: Dict) -> str:
    if event["type"] in ("text", "audio"):
        return "Necesito una foto o PDF del recibo para completar la extraccion."
    if event["type"] == "image":
        return "Procesando imagen con OCR..."
    return "Evento recibido."
