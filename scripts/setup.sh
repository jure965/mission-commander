#!/bin/bash -xe

cp scripts/*.service /etc/systemd/system

/root/.local/bin/poetry install --no-root --without dev
/root/.local/bin/poetry run python manage.py migrate
/root/.local/bin/poetry run python manage.py collectstatic --noinput

systemctl daemon-reload
systemctl start mc-web.service mc-beat.service mc-worker.service
systemctl enable mc-web.service mc-beat.service mc-worker.service
