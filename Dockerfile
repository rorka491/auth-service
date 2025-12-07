FROM python:3.13-slim

WORKDIR /app



RUN pip install uv

COPY . .

RUN openssl genrsa -out /app/private.pem 2048 && \
    openssl rsa -in /app/private.pem -pubout -out /app/public.pem

RUN uv sync --frozen




CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



