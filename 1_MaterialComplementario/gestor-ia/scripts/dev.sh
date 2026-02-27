#!/usr/bin/env bash
set -euo pipefail

docker-compose up -d

echo "Starting API..."
(
  cd apps/api
  if [ ! -d ".venv" ]; then
    python -m venv .venv
  fi
  source .venv/bin/activate
  pip install -r requirements.txt
  alembic upgrade head
  python -m app.db.seed
  uvicorn app.main:app --reload --port 8000
)

echo "Starting Web..."
(
  cd apps/web
  npm install
  npm run dev
)
