#!/bin/bash

systemctl stop mc-web.service mc-beat.service mc-worker.service

uv run install --sync --no-root --without dev
uv run python manage.py migrate
uv run python manage.py collectstatic --noinput

systemctl start mc-web.service mc-beat.service mc-worker.service
