from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = (
    "django-insecure-!_l*vnip4xjc$uei$y(__k70qd4024#i0lz=1%i1x&u05k$l^#"
)

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "drf_spectacular",

    "post",
    "user",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "user.middleware.UpdateLastLoginMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "social_network.urls"

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

WSGI_APPLICATION = "social_network.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation."
                "UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation."
                "MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation."
                "CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation."
                "NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "user.User"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Kiev"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

SIMPLE_JWT = {
    "USER_ID_FIELD": "email",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Social Network",
    "DESCRIPTION": "Project for managing analytics about posts",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "defaultModelRendering": "model",
        "defaultModelsExpandDepth": 2,
        "defaultModelExpandDepth": 2,
    },
}
