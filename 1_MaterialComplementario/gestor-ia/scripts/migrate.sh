#!/usr/bin/env bash
set -euo pipefail

cd apps/api
if [ ! -d ".venv" ]; then
  python -m venv .venv
fi
source .venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
