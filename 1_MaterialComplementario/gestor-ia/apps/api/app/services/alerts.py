import json
import os
from typing import Dict, List


FIXTURES_PATH = os.path.join(os.path.dirname(__file__), "..", "fixtures")


def load_boe_changes() -> List[Dict]:
    with open(os.path.join(FIXTURES_PATH, "boe_changes.json"), "r", encoding="utf-8") as fh:
        return json.load(fh)


def load_dehu_forwards() -> List[Dict]:
    with open(os.path.join(FIXTURES_PATH, "dehu_forwards.json"), "r", encoding="utf-8") as fh:
        return json.load(fh)
