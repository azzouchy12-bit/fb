from datetime import timedelta
import hashlib
import os
from pathlib import Path
from urllib.parse import urlparse

import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent


def env_bool(name, default=False):
    return os.getenv(name, str(default)).strip().lower() in {"1", "true", "yes", "on"}


def env_list(name, default=""):
    raw_value = os.getenv(name, default)
    return [item.strip() for item in raw_value.split(",") if item.strip()]


def unique(items):
    seen = set()
    result = []
    for item in items:
        if item and item not in seen:
            seen.add(item)
            result.append(item)
    return result


def normalize_host(value):
    if not value:
        return ""

    cleaned = value.strip().strip("/")
    if "://" in cleaned:
        cleaned = urlparse(cleaned).netloc

    return cleaned.strip()


def normalize_origin(value):
    if not value:
        return ""

    cleaned = value.strip().rstrip("/")
    if not cleaned:
        return ""
    if "://" not in cleaned:
        cleaned = f"https://{cleaned}"

    parsed = urlparse(cleaned)
    if not parsed.scheme or not parsed.netloc:
        return ""

    return f"{parsed.scheme}://{parsed.netloc}"


IS_RAILWAY = any(
    os.getenv(name)
    for name in ("RAILWAY_ENVIRONMENT", "RAILWAY_PROJECT_ID", "RAILWAY_SERVICE_ID")
)

railway_public_domain = normalize_host(os.getenv("RAILWAY_PUBLIC_DOMAIN", ""))
railway_static_domain = normalize_host(os.getenv("RAILWAY_STATIC_URL", ""))
railway_private_domain = normalize_host(os.getenv("RAILWAY_PRIVATE_DOMAIN", ""))


def generated_secret_key():
    seed_parts = [
        os.getenv("RAILWAY_PROJECT_ID", ""),
        os.getenv("RAILWAY_SERVICE_ID", ""),
        os.getenv("RAILWAY_ENVIRONMENT_ID", ""),
        railway_public_domain,
        railway_private_domain,
    ]
    seed = "|".join(part for part in seed_parts if part)
    if not seed:
        seed = "local-development-only"

    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    return f"django-insecure-{digest}"


SECRET_KEY = os.getenv("SECRET_KEY") or generated_secret_key()
DEBUG = env_bool("DEBUG", not IS_RAILWAY)

WEBSITE_URL = normalize_origin(
    os.getenv(
        "WEBSITE_URL",
        railway_public_domain or railway_static_domain or "http://127.0.0.1:8000",
    )
)

ALLOWED_HOSTS = unique(
    env_list("ALLOWED_HOSTS", "")
    + [
        "127.0.0.1",
        "localhost",
        railway_public_domain,
        railway_static_domain,
        railway_private_domain,
        normalize_host(WEBSITE_URL),
    ]
)


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
    "CORS_ALLOWED_ORIGINS", ""
)

frontend_origins = env_list("FRONTEND_URLS", "")
frontend_origin = normalize_origin(os.getenv("FRONTEND_URL", ""))
if frontend_origin:
    frontend_origins.append(frontend_origin)

if not IS_RAILWAY:
    frontend_origins.extend(["http://localhost:5173", "http://localhost:5174"])

CORS_ALLOWED_ORIGINS = unique(
    [normalize_origin(origin) for origin in CORS_ALLOWED_ORIGINS + frontend_origins]
    + [WEBSITE_URL]
)

CORS_ALLOW_ALL_ORIGINS = env_bool(
    "CORS_ALLOW_ALL_ORIGINS", IS_RAILWAY and not CORS_ALLOWED_ORIGINS
)

CSRF_TRUSTED_ORIGINS = unique(
    [normalize_origin(origin) for origin in env_list("CSRF_TRUSTED_ORIGINS", "")]
    + CORS_ALLOWED_ORIGINS
    + [WEBSITE_URL]
)


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
database_url = os.getenv("DATABASE_URL") or default_sqlite_url
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
