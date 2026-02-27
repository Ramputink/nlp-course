import re
from typing import Dict, Tuple


def validate_nif_cif(value: str) -> bool:
    if not value:
        return False
    return bool(re.match(r"^([0-9]{8}[A-Z]|[A-Z][0-9]{8})$", value))


def validate_amounts(total: float, vat: float) -> bool:
    if total <= 0:
        return False
    if vat < 0:
        return False
    return True


def validate_date(value: str) -> bool:
    return bool(re.match(r"^\\d{4}-\\d{2}-\\d{2}$", value or ""))


def confidence_score(payload: Dict) -> Tuple[float, Dict]:
    checks = {
        "nif_cif": validate_nif_cif(payload.get("nif") or payload.get("cif", "")),
        "amounts": validate_amounts(payload.get("total", 0), payload.get("vat", 0)),
        "date": validate_date(payload.get("date", "")),
    }
    score = sum(1 for v in checks.values() if v) / max(len(checks), 1)
    return score, checks
