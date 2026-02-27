"""initial schema

Revision ID: 0001_initial
Revises: 
Create Date: 2026-02-03
"""
from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import Vector


revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")

    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String, nullable=False),
        sa.Column("role", sa.String, nullable=False),
        sa.Column("locale", sa.String, nullable=False),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
    )
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    op.create_table(
        "profiles",
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), primary_key=True),
        sa.Column("provincia", sa.String),
        sa.Column("regimen_autonomo", sa.String),
        sa.Column("actividad", sa.String),
        sa.Column("start_date", sa.Date),
        sa.Column("retention_days", sa.Integer),
    )

    op.create_table(
        "documents",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id")),
        sa.Column("type", sa.String, nullable=False),
        sa.Column("filename", sa.String, nullable=False),
        sa.Column("storage_path", sa.String, nullable=False),
        sa.Column("extracted_json", sa.JSON),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
    )

    op.create_table(
        "expenses",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id")),
        sa.Column("vendor", sa.String, nullable=False),
        sa.Column("date", sa.Date, nullable=False),
        sa.Column("total", sa.Float, nullable=False),
        sa.Column("vat", sa.Float),
        sa.Column("category", sa.String),
        sa.Column("confidence", sa.Float),
        sa.Column("source_document_id", sa.Integer, sa.ForeignKey("documents.id")),
    )

    op.create_table(
        "invoices",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id")),
        sa.Column("client_name", sa.String, nullable=False),
        sa.Column("client_nif", sa.String),
        sa.Column("date", sa.Date, nullable=False),
        sa.Column("total", sa.Float, nullable=False),
        sa.Column("vat", sa.Float),
        sa.Column("status", sa.String, nullable=False),
    )

    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id")),
        sa.Column("type", sa.String, nullable=False),
        sa.Column("due_date", sa.Date),
        sa.Column("status", sa.String, nullable=False),
        sa.Column("metadata_json", sa.JSON),
    )

    op.create_table(
        "filings",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id")),
        sa.Column("model", sa.String, nullable=False),
        sa.Column("period", sa.String, nullable=False),
        sa.Column("draft_json", sa.JSON),
        sa.Column("status", sa.String, nullable=False),
        sa.Column("submitted_at", sa.DateTime),
    )

    op.create_table(
        "sources",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("jurisdiction", sa.String, nullable=False),
        sa.Column("agency", sa.String, nullable=False),
        sa.Column("title", sa.String, nullable=False),
        sa.Column("url", sa.String, nullable=False),
        sa.Column("fetched_at", sa.DateTime, server_default=sa.func.now()),
        sa.Column("content_hash", sa.String, nullable=False),
        sa.Column("raw_text_path", sa.String, nullable=False),
        sa.Column("embedding", Vector(8)),
    )

    op.create_table(
        "answers",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id")),
        sa.Column("question", sa.Text, nullable=False),
        sa.Column("answer_text", sa.Text, nullable=False),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
    )

    op.create_table(
        "citations",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("answer_id", sa.Integer, sa.ForeignKey("answers.id")),
        sa.Column("source_id", sa.Integer, sa.ForeignKey("sources.id")),
        sa.Column("url", sa.String, nullable=False),
        sa.Column("snippet", sa.Text, nullable=False),
        sa.Column("as_of_date", sa.String, nullable=False),
    )

    op.create_table(
        "audit_log",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id")),
        sa.Column("action", sa.String, nullable=False),
        sa.Column("entity_type", sa.String, nullable=False),
        sa.Column("entity_id", sa.Integer),
        sa.Column("before_json", sa.JSON),
        sa.Column("after_json", sa.JSON),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
    )

    op.create_table(
        "partner_reviews",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("filing_id", sa.Integer, sa.ForeignKey("filings.id")),
        sa.Column("partner_user_id", sa.Integer, sa.ForeignKey("users.id")),
        sa.Column("status", sa.String, nullable=False),
        sa.Column("notes", sa.Text),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
    )

    op.create_table(
        "alerts",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id")),
        sa.Column("type", sa.String, nullable=False),
        sa.Column("title", sa.String, nullable=False),
        sa.Column("body", sa.Text, nullable=False),
        sa.Column("severity", sa.String, nullable=False),
        sa.Column("status", sa.String, nullable=False),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
    )

    op.create_table(
        "whatsapp_events",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id")),
        sa.Column("type", sa.String, nullable=False),
        sa.Column("payload_json", sa.JSON, nullable=False),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table("whatsapp_events")
    op.drop_table("alerts")
    op.drop_table("partner_reviews")
    op.drop_table("audit_log")
    op.drop_table("citations")
    op.drop_table("answers")
    op.drop_table("sources")
    op.drop_table("filings")
    op.drop_table("tasks")
    op.drop_table("invoices")
    op.drop_table("expenses")
    op.drop_table("documents")
    op.drop_table("profiles")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")
