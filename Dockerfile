# Builder stage
FROM python:3.11-slim AS builder

ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /code
COPY pyproject.toml /code/

# Installing system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends  \
    build-essential \
    libpq-dev \
    && pip install --no-cache-dir --upgrade pip setuptools poetry \
    && rm -rf /var/lib/apt/lists/*

# Installing Poetry dependencies
ARG DEBUG
RUN poetry install $(if [ "$DEBUG" = "False" ]; then echo "--no-dev"; fi) \
    && poetry cache clear . --all


# Base stage
FROM python:3.11-slim AS base

ENV PYTHONUNBUFFERED=1

WORKDIR /code

# Copying installed dependencies from the builder stage
COPY --from=builder /usr/local /usr/local

# Copying project source code
COPY . /code/
