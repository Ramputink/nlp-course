# Gestor.ia (MVP monorepo)

Autonomo Copilot + Bureaucracy Navigator para autonomos en Espana. Incluye RAG gov-only (AEAT/BOE/DEHU), experiencia zero-admin via WhatsApp (simulada), OCR/extraccion simulada, y flujos end-to-end con datos mock.

## Arquitectura
- Frontend: Next.js + TypeScript + Tailwind (mockup navegable, datos reales desde API)
- Backend: FastAPI + SQLAlchemy + Alembic + RQ (Redis)
- DB: Postgres + pgvector
- Storage: filesystem local (preparado para S3-compatible)
- Auth: magic link mock + JWT
- Observabilidad: logs estructurados + health endpoints

## Requisitos
- Docker + Docker Compose
- Node.js 18+ (para frontend)
- Python 3.11+

## Quickstart (todo local)
1) Copia envs:
   - `cp .env.example .env`
   - `cp apps/api/.env.example apps/api/.env`
   - `cp apps/web/.env.example apps/web/.env.local`
2) Infra (Postgres + Redis):
   - `docker-compose up -d`
3) Backend:
   - `cd apps/api`
   - `python -m venv .venv && source .venv/bin/activate`
   - `pip install -r requirements.txt`
   - `alembic upgrade head`
   - `python -m app.db.seed`
   - `uvicorn app.main:app --reload --port 8000`
   - En otra terminal (jobs): `python -m app.jobs.worker`
4) Frontend:
   - `cd apps/web`
   - `npm install`
   - `npm run dev`
5) Abre:
   - Frontend: http://localhost:3000
   - API: http://localhost:8000/docs

## Scripts (root)
- `scripts/dev.sh` -> levanta docker + api + web (basico)
- `scripts/test.sh` -> tests (placeholder)
- `scripts/lint.sh` -> lint (placeholder)
- `scripts/migrate.sh` -> alembic upgrade head
- `scripts/seed.sh` -> seed data mock

## Flujos end-to-end incluidos (mock)
1) WhatsApp text/audio -> crea expense -> pide foto -> OCR fixture -> categorizacion -> aparece en dashboard.
2) Pregunta RAG -> respuesta con 2-5 citas -> vista de fuente con snippet resaltado.
3) BOE change job -> crea alert -> aparece en notificaciones con "que cambia para ti".
4) DEHU forwarded PDF -> parse -> resumen -> draft respuesta -> opcion enviar (mock).
5) Draft filing (modelo 303 placeholder) -> partner review -> aprobar -> listo para presentar.

## Notas de RAG
- Solo fuentes gov (AEAT/BOE/DEHU). Si una fuente no es gov, se rechaza.
- Cada afirmacion relevante incluye citas con: source_id, url, snippet, as_of_date.
- Viewer de fuente: `GET /sources/{id}` resalta el texto citado.

## Seguridad / GDPR (MVP serio)
- Roles: user, partner_gestor, admin
- Encriptacion app-level (NIF/IBAN)
- Retencion configurable + exportacion de datos
- Audit log append-only

## Deploy
- `docker-compose up -d`
- Ajusta envs en `.env` y `apps/api/.env`
- Build web: `npm run build`
