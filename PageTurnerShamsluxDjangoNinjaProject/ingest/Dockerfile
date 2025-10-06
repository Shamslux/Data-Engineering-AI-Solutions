FROM python:3.12-slim

WORKDIR /work
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /work/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ingest.py /work/ingest.py

CMD ["python", "/work/ingest.py"]
