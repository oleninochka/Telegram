# CTF Platform Telegram

## Quickstart

### Configuration

Copy env file and replace variables with your preferred values:

```bash
cp deploy/config/.env.sample deploy/config/.env
```

Create virtual environment:

```bash
python3 -m venv .venv
```

Install dependencies:

```bash
poetry install
```

### Run in development environment

```bash
python3 ./app/main.py
```
