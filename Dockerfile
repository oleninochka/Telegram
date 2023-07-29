FROM python:3.11-slim as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

RUN apt update && apt install -y \
    python3-dev \
    build-essential \
    libssl-dev \
    default-libmysqlclient-dev \
    pkg-config

FROM base as builder

RUN pip install poetry

COPY pyproject.toml pyproject.toml

RUN poetry install --no-dev --no-root

COPY . .

RUN poetry build

FROM base as final

COPY --from=builder /app .

RUN pip install --no-cache /app/dist/*.whl

WORKDIR /app/app
