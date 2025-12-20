#!/bin/bash
set -e

# Ждём доступности PostgreSQL
echo "Waiting for PostgreSQL..."
for i in {1..30}; do
  python -c "import psycopg2; psycopg2.connect(os.environ.get('DATABASE_URL', 'postgresql://superset:superset@postgres:5432/superset'))" 2>/dev/null && break
  echo "Attempt $i/30 - PostgreSQL not ready, waiting..."
  sleep 2
done

# create Admin user
superset fab create-admin --username "$ADMIN_USERNAME" --firstname Superset --lastname Admin --email "$ADMIN_EMAIL" --password "$ADMIN_PASSWORD"

# Upgrading Superset metastore
superset db upgrade

# setup roles and permissions
superset superset init 

# Starting server
/bin/sh -c /usr/bin/run-server.sh