# CTF Platform Telegram

## Quickstart

### Requirements

**Development:**

- Python 3.11
- Poetry

**Deploy:**

- Docker
- Docker Compose

### Configuration

Copy env file and replace variables with your preferred values:

```bash
cp deploy/config/.env.sample deploy/config/.env
```

### Run in development environment

Create virtual environment:

```bash
python3 -m venv .venv
```

Activate virtual environment:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
poetry install
```

Copy env file:

```bash
cp deploy/config/.env app/.env
```

Run project:

```bash
cd app && python3 main.py
```

### Run in production environment

Build and run containers:

```bash
cd deploy && docker compose up -d
```
