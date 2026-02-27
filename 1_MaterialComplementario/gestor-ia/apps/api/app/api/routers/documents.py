from fastapi import APIRouter, UploadFile, File, Form
import redis
from rq import Queue

from app.core.config import settings
from app.services.storage import save_file
from app.jobs import tasks


router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/upload")
def upload_document(user_id: int = Form(...), file: UploadFile = File(...)):
    saved_path = save_file(file.file, file.filename)
    redis_conn = redis.from_url(settings.redis_url)
    q = Queue("default", connection=redis_conn)
    job = q.enqueue(tasks.process_ocr, user_id, file.filename)
    return {"status": "queued", "job_id": job.id, "path": saved_path}
