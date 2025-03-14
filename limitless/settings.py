"""Django settings for limitless project."""

import os
from importlib import metadata
from pathlib import Path

from django.utils.translation import gettext_lazy

from limitless.utils import parse_bool_flag, parse_str_list

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
DEBUG = parse_bool_flag(env="DJANGO_DEBUG")
ALLOWED_HOSTS = parse_str_list(env="DJANGO_ALLOWED_HOSTS")
CSRF_TRUSTED_ORIGINS = parse_str_list(env="DJANGO_CSRF_TRUSTED_ORIGINS")

PROJECT_NAME = "limitless"
VERSION = metadata.version(PROJECT_NAME)
PROJECT_ID: str = f"{PROJECT_NAME}-v{VERSION}"

# HTTPOnly cookie settings

CSRF_COOKIE_HTTPONLY = False  # Needed by the Frontend
LANGUAGE_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True

# Application definition

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd Party
    "django_vite",
    "rest_framework",
    # limitless Apps
    "users.apps.UsersConfig",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "limitless.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "limitless/templates/",
        ],
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

WSGI_APPLICATION = "limitless.wsgi.application"

# Rest Framework

REST_FRAMEWORK: dict = {
    "DEFAULT_PERMISSION_CLASSES": [],
    "DEFAULT_AUTHENTICATION_CLASSES": [],
}

# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ.get("DJANGO_DATABASE_HOST"),
        "USER": os.environ.get("DJANGO_DATABASE_USER"),
        "PASSWORD": os.environ.get("DJANGO_DATABASE_PASSWORD"),
        "NAME": os.environ.get("DJANGO_DATABASE_NAME"),
        "PORT": 5432,
    }
}


# Password validation

VALIDATORS = "django.contrib.auth.password_validation."

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": VALIDATORS + "CommonPasswordValidator"},
    {"NAME": VALIDATORS + "MinimumLengthValidator"},
    {"NAME": VALIDATORS + "NumericPasswordValidator"},
    {"NAME": VALIDATORS + "UserAttributeSimilarityValidator"},
]

# Internationalization

USE_TZ = True
TIME_ZONE = "America/Toronto"

USE_I18N = True
LANGUAGE_CODE = "en-us"
LANGUAGES = [
    ("en-us", gettext_lazy("English (US)")),
    ("en-ca", gettext_lazy("English (Canada)")),
    ("en-gb", gettext_lazy("English (UK)")),
    ("en-au", gettext_lazy("English (Australia)")),
]

LOCALE_PATHS = [BASE_DIR / "locale/"]

# Django Vite

DJANGO_VITE_ASSETS_PATH = BASE_DIR / "frontend/dist/"
DJANGO_VITE_DEV_MODE = DEBUG  # HMR Mode depends on Debug flag
DJANGO_VITE_STATIC_URL_PREFIX = "frontend"

# Static files (CSS, JavaScript, Images)

STATIC_ROOT = "/var/opt/limitless/static/"
STATICFILES_DIRS = [
    BASE_DIR / "limitless/static/",
    DJANGO_VITE_ASSETS_PATH,
]

STATIC_URL = "static/"
STATICFILES_STORAGE = (
    "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
)

# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Authentication

AUTH_USER_MODEL = "users.User"
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "users:welcome"
LOGOUT_REDIRECT_URL = "login"

# Media Storage

MEDIA_ROOT = BASE_DIR / "media/"
MEDIA_URL = "media/"

MAX_UPLOAD_SIZE: int = 50  # MB

THUMBNAIL_SIZE: tuple[int, int] = (120, 120)
PDF_THUMBNAIL_DPI: int = 75

# Logging

LOG_LEVEL = os.getenv("DJANGO_LOG_LEVEL", "INFO")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "()": "limitless.formatters.UTCFormatter",
            "format": "%(asctime)s [%(levelname)-8s] %(message)s",
            "datefmt": "%H:%M:%S %Z",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG" if DEBUG else "INFO",
            "formatter": "console",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
            "propagate": False if DEBUG else True,
        },
        "limitless": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
        "asyncio": {
            "level": "WARNING",
        },
    },
}
