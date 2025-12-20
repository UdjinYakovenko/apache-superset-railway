import os
from datetime import timedelta

FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "ALERT_REPORTS": True,
}

PREVENT_UNSAFE_DB_CONNECTIONS = False
ENABLE_PROXY_FIX = True

ALERT_REPORTS = True

SECRET_KEY = os.environ.get("SECRET_KEY", "your-secret-key-change-in-production")

# ===== DATABASE CONFIGURATION =====
# Railway автоматически inject DATABASE_URL
DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    # Fallback для локальной разработки
    DATABASE_URL = "postgresql://superset:superset@postgres:5432/superset"

SQLALCHEMY_DATABASE_URI = DATABASE_URL

# ===== ALERT & REPORT CONFIGURATION =====
ALERT_REPORTS_WORKING_TIME_OUT = 300
ALERT_REPORTS_CHUNKSIZE = 5000
ALERT_REPORTS_MAX_RETRIES = 5
ALERT_REPORTS_CRON_INTERVAL = 60

# ===== CELERY CONFIGURATION =====
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60  # 30 minutes
CELERY_TASK_SOFT_TIME_LIMIT = 25 * 60  # 25 minutes

# ===== SMTP CONFIGURATION =====
SMTP_HOST = os.environ.get("SMTP_HOST", "localhost")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
SMTP_STARTTLS = os.environ.get("SMTP_STARTTLS", "true").lower() == "true"
SMTP_SSL = os.environ.get("SMTP_SSL", "false").lower() == "true"
SMTP_USER = os.environ.get("SMTP_USER", "")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "")
SMTP_MAIL_FROM = os.environ.get("SMTP_MAIL_FROM", "superset@example.com")

# ===== CACHE CONFIGURATION =====
CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_REDIS_URL": os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/1"),
    "CACHE_DEFAULT_TIMEOUT": 60,
}

# ===== SESSION CONFIGURATION =====
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
