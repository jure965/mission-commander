FROM python:3.12-slim

ENV PYTHONFAULTHANDLER=1 \
PYTHONUNBUFFERED=1 \
PYTHONHASHSEED=random \
PIP_NO_CACHE_DIR=off \
PIP_DISABLE_PIP_VERSION_CHECK=on \
PIP_DEFAULT_TIMEOUT=100 \
POETRY_VERSION=1.8.2 \
POETRY_VIRTUALENVS_CREATE=false \
POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN pip3 install poetry

WORKDIR /code

COPY poetry.lock pyproject.toml /code/

RUN poetry install --no-root --without dev

COPY . /code/

USER 1000
