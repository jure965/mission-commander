#!/bin/bash

systemctl stop mc-web.service mc-beat.service mc-worker.service

/root/.local/bin/poetry install --remove-untracked --no-root --without dev
/root/.local/bin/poetry run python manage.py migrate
/root/.local/bin/poetry run python manage.py collectstatic --noinput

systemctl start mc-web.service mc-beat.service mc-worker.service
