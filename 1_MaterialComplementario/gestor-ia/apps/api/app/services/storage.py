import os
from typing import BinaryIO

from app.core.config import settings


def save_file(fileobj: BinaryIO, filename: str) -> str:
    os.makedirs(settings.storage_path, exist_ok=True)
    path = os.path.join(settings.storage_path, filename)
    with open(path, "wb") as fh:
        fh.write(fileobj.read())
    return path
