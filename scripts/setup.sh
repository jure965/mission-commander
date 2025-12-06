#!/bin/bash -xe

cp scripts/*.service /etc/systemd/system

uv install --no-root --without dev
uv run python manage.py migrate
uv run python manage.py collectstatic --noinput

systemctl daemon-reload
systemctl start mc-web.service mc-beat.service mc-worker.service
systemctl enable mc-web.service mc-beat.service mc-worker.service
