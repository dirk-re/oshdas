#!/usr/bin/env bash
# Fuehrt manage.py mit den Umgebungsvariablen aus .env aus, damit CLI und
# Server (start.sh) immer dieselbe Konfiguration sehen.
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

exec "$PYTHON" manage.py "$@"
