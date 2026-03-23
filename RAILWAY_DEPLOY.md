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

## 3) Add PostgreSQL
1. Inside the same Railway project, add a **PostgreSQL** service.
2. Railway will inject `DATABASE_URL` automatically.

## 4) Configure required environment variables
In the web service Variables tab, set:
- `SECRET_KEY` = any long random secret
- `DEBUG` = `False`
- `ALLOWED_HOSTS` = your Railway domain host (for example: `your-app.up.railway.app`)
- `WEBSITE_URL` = full https URL (for example: `https://your-app.up.railway.app`)
- `CORS_ALLOWED_ORIGINS` = your frontend URL(s), comma-separated
- `CSRF_TRUSTED_ORIGINS` = your frontend URL(s), comma-separated

Optional email settings are available in `.env.example`.

## 5) Deploy
Railway will run:
- `python manage.py migrate`
- `python manage.py collectstatic --noinput`
- `gunicorn facebook_django.wsgi:application --bind 0.0.0.0:$PORT`

## 6) Verify
After deploy:
- Open `/admin/login/` on your Railway URL for a quick health check.
- API base path is `/api/`.
