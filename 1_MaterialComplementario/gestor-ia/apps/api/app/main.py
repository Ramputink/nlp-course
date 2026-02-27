from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.logging import configure_logging
from app.api.routers import (
    health,
    auth,
    profile,
    expenses,
    rag,
    sources,
    alerts,
    whatsapp,
    documents,
    filings,
    partners,
    data,
)


configure_logging()

app = FastAPI(title="Gestor.ia API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(expenses.router)
app.include_router(rag.router)
app.include_router(sources.router)
app.include_router(alerts.router)
app.include_router(whatsapp.router)
app.include_router(documents.router)
app.include_router(filings.router)
app.include_router(partners.router)
app.include_router(data.router)
