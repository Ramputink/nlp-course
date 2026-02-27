from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Date,
    Float,
    ForeignKey,
    JSON,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from pgvector.sqlalchemy import Vector

from app.db.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(String, default="user", nullable=False)
    locale = Column(String, default="es-ES", nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    profile = relationship("Profile", back_populates="user", uselist=False)


class Profile(Base):
    __tablename__ = "profiles"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    provincia = Column(String, nullable=True)
    regimen_autonomo = Column(String, nullable=True)
    actividad = Column(String, nullable=True)
    start_date = Column(Date, nullable=True)
    retention_days = Column(Integer, nullable=True)

    user = relationship("User", back_populates="profile")


class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String, nullable=False)
    filename = Column(String, nullable=False)
    storage_path = Column(String, nullable=False)
    extracted_json = Column(JSON, nullable=True)
    created_at = Column(DateTime, server_default=func.now())


class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    vendor = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    total = Column(Float, nullable=False)
    vat = Column(Float, nullable=True)
    category = Column(String, nullable=True)
    confidence = Column(Float, nullable=True)
    source_document_id = Column(Integer, ForeignKey("documents.id"), nullable=True)


class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    client_name = Column(String, nullable=False)
    client_nif = Column(String, nullable=True)
    date = Column(Date, nullable=False)
    total = Column(Float, nullable=False)
    vat = Column(Float, nullable=True)
    status = Column(String, default="draft", nullable=False)


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String, nullable=False)
    due_date = Column(Date, nullable=True)
    status = Column(String, default="pending", nullable=False)
    metadata_json = Column(JSON, nullable=True)


class Filing(Base):
    __tablename__ = "filings"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    model = Column(String, nullable=False)
    period = Column(String, nullable=False)
    draft_json = Column(JSON, nullable=True)
    status = Column(String, default="draft", nullable=False)
    submitted_at = Column(DateTime, nullable=True)


class Source(Base):
    __tablename__ = "sources"
    id = Column(Integer, primary_key=True)
    jurisdiction = Column(String, nullable=False)
    agency = Column(String, nullable=False)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    fetched_at = Column(DateTime, server_default=func.now())
    content_hash = Column(String, nullable=False)
    raw_text_path = Column(String, nullable=False)
    embedding = Column(Vector(8), nullable=True)


class Answer(Base):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question = Column(Text, nullable=False)
    answer_text = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())


class Citation(Base):
    __tablename__ = "citations"
    id = Column(Integer, primary_key=True)
    answer_id = Column(Integer, ForeignKey("answers.id"))
    source_id = Column(Integer, ForeignKey("sources.id"))
    url = Column(String, nullable=False)
    snippet = Column(Text, nullable=False)
    as_of_date = Column(String, nullable=False)


class AuditLog(Base):
    __tablename__ = "audit_log"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String, nullable=False)
    entity_type = Column(String, nullable=False)
    entity_id = Column(Integer, nullable=True)
    before_json = Column(JSON, nullable=True)
    after_json = Column(JSON, nullable=True)
    created_at = Column(DateTime, server_default=func.now())


class PartnerReview(Base):
    __tablename__ = "partner_reviews"
    id = Column(Integer, primary_key=True)
    filing_id = Column(Integer, ForeignKey("filings.id"))
    partner_user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String, default="pending", nullable=False)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now())


class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String, nullable=False)
    title = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    severity = Column(String, default="info", nullable=False)
    status = Column(String, default="unread", nullable=False)
    created_at = Column(DateTime, server_default=func.now())


class WhatsappEvent(Base):
    __tablename__ = "whatsapp_events"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String, nullable=False)
    payload_json = Column(JSON, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
