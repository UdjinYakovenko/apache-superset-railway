# Apache Superset на Railway с Алёртами

## 🚀 Деплой на Railway

### Шаг 1: Подготовка репозитория
```bash
git add .
git commit -m "Add Railway configuration for Superset with alerts"
git push
```

### Шаг 2: Создание проекта на Railway
1. Перейти на [railway.app](https://railway.app)
2. Нажать "New Project" → "Deploy from GitHub"
3. Выбрать репозиторий `apache-superset-railway`

### Шаг 3: Добавить сервисы
Railway автоматически найдёт `railway.json` и создаст:

#### PostgreSQL (встроенный)
- Railway автоматически создаст PostgreSQL
- Переменные окружения (автоматически):
  - `DATABASE_URL` - строка подключения
  - `PGHOST`, `PGPORT`, `PGUSER`, `PGPASSWORD`, `PGDATABASE`

#### Redis (встроенный)
- Railway автоматически создаст Redis  
- Переменные окружения (автоматически):
  - `REDIS_URL` или `REDIS_PRIVATE_URL` - строка подключения

#### Superset Web Service
- **Service**: `superset`
- **Port**: 8088
- **Dockerfile**: `Dockerfile`

#### Superset Worker Service  
- **Service**: `superset-worker`
- **Dockerfile**: `Dockerfile.worker`

### Шаг 4: Установить переменные окружения

В Railway Dashboard → Variables добавить:

```
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=your_secure_password_here
SECRET_KEY=your_secret_key_change_in_production

SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_STARTTLS=true
SMTP_SSL=false
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password
SMTP_MAIL_FROM=superset@yourdomain.com
```

**Для Gmail:**
1. Включить 2FA в аккаунте Google
2. Создать "App Password" [здесь](https://myaccount.google.com/apppasswords)
3. Использовать сгенерированный пароль в `SMTP_PASSWORD`

### Шаг 5: Деплой

Railway автоматически:
1. Создаст PostgreSQL и Redis
2. Развернёт Superset Web на порту 8088
3. Развернёт Celery Worker для обработки алёртов
4. Инициализирует БД и создаст admin пользователя

## 📋 Архитектура

```
┌─────────────────────────────────────────┐
│         Railway Platform                 │
├─────────────────────────────────────────┤
│                                         │
│  ┌──────────────┐  ┌──────────────┐   │
│  │ Superset Web │  │ Superset     │   │
│  │ (port 8088)  │  │ Worker       │   │
│  │              │  │ (Celery)     │   │
│  └────────┬─────┘  └──────┬───────┘   │
│           │                │            │
│  ┌────────▼────────────────▼─────┐    │
│  │   PostgreSQL + Redis (managed) │    │
│  └────────────────────────────────┘    │
│                                         │
└─────────────────────────────────────────┘
```

## 🔐 Безопасность

- `SESSION_COOKIE_SECURE=True` - HTTPS only
- `SESSION_COOKIE_HTTPONLY=True` - защита от XSS
- `SQLALCHEMY_DATABASE_URI` - переменная окружения (не в коде)
- Все пароли в переменных Railway, не в репозитории

## 📊 Использование Алёртов

После деплоя:

1. Перейти на http://your-railway-url:8088
2. Логин: admin / пароль из `ADMIN_PASSWORD`
3. Создать дашборд и настроить алёрты
4. Worker автоматически обработает их по расписанию

## 🆘 Решение проблем

### Alerm не отправляются
- Проверить логи Worker: Railway Dashboard → superset-worker → Logs
- Проверить SMTP переменные
- Проверить Redis подключение

### Ошибка подключения к БД
```bash
# Railway автоматически inject DATABASE_URL
# Проверить в переменных окружения сервиса
```

### Worker крашится
- Посмотреть логи: Railway Dashboard → superset-worker → Logs
- Проверить Redis URL доступна

## 🔄 Локальная разработка

Для локальной разработки используйте `docker-compose.yml`:

```bash
cp .env.example .env
docker-compose up -d
```

Superset: http://localhost:8088

---

**Вопросы?** Посмотрите:
- [Railway Docs](https://docs.railway.app)
- [Superset Docs](https://superset.apache.org)
