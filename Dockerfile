FROM apache/superset:latest

USER root

RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev \
    unixodbc \
    unixodbc-dev \
    libpq-dev \
    gcc \
    g++ \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN . /app/.venv/bin/activate && \
    uv pip install \
        psycopg2-binary \
        pymongo \
        pymssql \
        pyodbc \
        mysqlclient \
        openpyxl \
        Pillow

ENV ADMIN_USERNAME $ADMIN_USERNAME
ENV ADMIN_EMAIL $ADMIN_EMAIL
ENV ADMIN_PASSWORD $ADMIN_PASSWORD

COPY /config/superset_config.py /app/pythonpath/superset_config.py
COPY /config/superset_init.sh /app/superset_init.sh
RUN chmod +x /app/superset_init.sh


ENV PYTHONPATH=/app/pythonpath \
    SUPERSET_CONFIG_PATH=/app/pythonpath/superset_config.py
ENV SECRET_KEY $SECRET_KEY

USER superset

ENTRYPOINT [ "/app/superset_init.sh" ]
