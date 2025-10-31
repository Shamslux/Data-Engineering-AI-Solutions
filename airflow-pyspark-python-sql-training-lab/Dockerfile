FROM apache/airflow:2.9.2

USER root
RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends openjdk-17-jre-headless; \
    rm -rf /var/lib/apt/lists/*

USER airflow
RUN pip install --no-cache-dir \
    pandas numpy pyspark==4.0.1 sqlalchemy psycopg2-binary \
    openpyxl xlsxwriter \
    requests httpx beautifulsoup4 \
    python-telegram-bot tqdm pyyaml selenium
