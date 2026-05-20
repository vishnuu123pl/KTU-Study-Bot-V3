FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# FIX: Copy source but NOT .env — credentials come from Koyeb env vars
COPY . .
RUN rm -f .env

CMD ["python", "web.py"]
