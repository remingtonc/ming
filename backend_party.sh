#!/usr/bin/env bash
#podman build -t ming-backend:0.0.1 backend/
podman run --publish=8000:8000 --env-file=backend/.env --network=ming --mount=type=bind,source=$(pwd)/backend/ming,destination=/app/ming localhost/ming-backend:0.0.1 --reload --reload-dir /app/ming --host 0.0.0.0 ming:app