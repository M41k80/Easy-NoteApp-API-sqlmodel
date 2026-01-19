FROM python:3.12-slim

# ─────────────────────────────────────
# Configuración base
# ─────────────────────────────────────
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ─────────────────────────────────────
# Dependencias
# ─────────────────────────────────────
RUN pip install --no-cache-dir uv

COPY requirements.txt .
RUN pip install --system --no-cache -r requirements.txt

# ─────────────────────────────────────
# Código
# ─────────────────────────────────────
COPY . .

# ─────────────────────────────────────
# Puerto (Render lo sobreescribe)
# ─────────────────────────────────────
EXPOSE 8000

# ─────────────────────────────────────
# Arranque con migraciones
# ─────────────────────────────────────
CMD alembic upgrade head && \
    gunicorn \
    -k uvicorn.workers.UvicornWorker \
    -w 1 \
    -b 0.0.0.0:${PORT:-8000} \
    app.main:app
