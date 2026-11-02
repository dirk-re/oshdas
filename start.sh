#!/usr/bin/env bash
# Startet den Dev-Server. Umgebungsvariablen werden aus .env exportiert
# (Werte mit Sonderzeichen in .env bitte in doppelte Anfuehrungszeichen setzen).
set -euo pipefail
cd "$(dirname "$0")"

if [ -f .env ]; then
  set -a
  # shellcheck disable=SC1091
  source .env
  set +a
fi

PYTHON="venv/bin/python"
[ -x "$PYTHON" ] || PYTHON=python3

exec "$PYTHON" manage.py runserver "${@:-0.0.0.0:8000}"
