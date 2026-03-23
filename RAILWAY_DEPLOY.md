# Deploy To Railway

## 1) Push the latest code
This repository is already configured with:
- `railway.json`
- `requirements.txt`
- production-ready Django settings using environment variables

## 2) Create a Railway project
1. Open Railway dashboard.
2. Create a new project from GitHub.
3. Select this repository: `azzouchy12-bit/fb`.

## 3) Import suggested variables (optional but recommended)
After linking GitHub, Railway can detect `.env.example` in repo root and show **Suggested Variables**.
Import them with one click.

## 4) Add PostgreSQL
1. Inside the same Railway project, add a **PostgreSQL** service.
2. Railway will inject `DATABASE_URL` automatically.

## 5) Deploy without manual variable setup
The project now auto-derives core settings on Railway using built-in variables like:
- `RAILWAY_PUBLIC_DOMAIN`
- `RAILWAY_PRIVATE_DOMAIN`
- `RAILWAY_PROJECT_ID`
- `RAILWAY_SERVICE_ID`
- `RAILWAY_ENVIRONMENT_ID`

You only need to set email variables if you want real SMTP email sending.

## 6) Deploy
Railway will run:
- `python manage.py migrate`
- `python manage.py collectstatic --noinput`
- `gunicorn facebook_django.wsgi:application --bind 0.0.0.0:$PORT`

## 7) Verify
After deploy:
- Open `/admin/login/` on your Railway URL for a quick health check.
- API base path is `/api/`.
