#!/bin/bash -ex

git pull --ff-only
docker compose -f docker-compose-prod.yml down
docker build -t mission-commander:latest .
docker compose -f docker-compose-prod.yml up -d postgres redis
docker compose -f docker-compose-prod.yml run web python manage.py migrate
docker compose -f docker-compose-prod.yml run web python manage.py collectstatic --noinput
docker compose -f docker-compose-prod.yml up -d
