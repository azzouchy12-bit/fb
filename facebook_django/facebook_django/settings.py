from datetime import timedelta
import os
from pathlib import Path

import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent


def env_bool(name, default=False):
    return os.getenv(name, str(default)).strip().lower() in {"1", "true", "yes", "on"}


def env_list(name, default=""):
    raw_value = os.getenv(name, default)
    return [item.strip() for item in raw_value.split(",") if item.strip()]


IS_RAILWAY = os.getenv("RAILWAY_ENVIRONMENT") is not None


SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-change-me")
DEBUG = env_bool("DEBUG", not IS_RAILWAY)

ALLOWED_HOSTS = env_list("ALLOWED_HOSTS", "127.0.0.1,localhost")
railway_host = os.getenv("RAILWAY_STATIC_URL")
if railway_host and railway_host not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(railway_host)

default_website_url = (
    f"https://{railway_host}" if railway_host else "http://127.0.0.1:8000"
)
WEBSITE_URL = os.getenv("WEBSITE_URL", default_website_url)


EMAIL_BACKEND = os.getenv(
    "EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend"
)
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_USE_TLS = env_bool("EMAIL_USE_TLS", True)
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
DEFAULT_FROM_EMAIL = os.getenv(
    "DEFAULT_FROM_EMAIL", EMAIL_HOST_USER or "noreply@example.com"
)


AUTH_USER_MODEL = "account.User"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=180),
    "ROTATE_REFRESH_TOKENS": False,
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

CORS_ALLOWED_ORIGINS = env_list(
    "CORS_ALLOWED_ORIGINS", "http://localhost:5173,http://localhost:5174"
)
CSRF_TRUSTED_ORIGINS = env_list(
    "CSRF_TRUSTED_ORIGINS", "http://localhost:5173,http://localhost:5174"
)
CORS_ALLOW_ALL_ORIGINS = env_bool("CORS_ALLOW_ALL_ORIGINS", False)

if railway_host:
    railway_origin = f"https://{railway_host}"
    if railway_origin not in CORS_ALLOWED_ORIGINS:
        CORS_ALLOWED_ORIGINS.append(railway_origin)
    if railway_origin not in CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.append(railway_origin)


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "account",
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "facebook_django.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "facebook_django.wsgi.application"

default_sqlite_url = f"sqlite:///{(BASE_DIR / 'db.sqlite3').as_posix()}"
database_url = os.getenv("DATABASE_URL", default_sqlite_url)
DATABASES = {"default": dj_database_url.parse(database_url, conn_max_age=600)}

if database_url.startswith("postgres"):
    DATABASES["default"]["OPTIONS"] = {"sslmode": os.getenv("PGSSLMODE", "require")}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


if IS_RAILWAY and not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = env_bool("SECURE_SSL_REDIRECT", True)
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
