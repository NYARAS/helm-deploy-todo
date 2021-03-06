"""Django settings for todo project."""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_bool_env(env_var, default=False):
    """Parse 'boolean' environment variable strings."""
    assert default is False or default is True
    val = os.getenv(env_var)
    import json

    if val is None:
        return default
    try:
        p = json.loads(val)
        assert p is False or p is True
        return p
    except ValueError:
        raise Exception("Invalid boolean config: {}".format(val))


# ======== start sanity tests for get_bool_env ================


var1, default1 = "tst-default-false", False
var2, default2 = "tst-default-true", True

assert get_bool_env(var1, default1) is False
assert get_bool_env(var2, default2) is True

os.environ[var1] = "false"
os.environ[var2] = "false"
assert get_bool_env(var1, default1) is False
assert get_bool_env(var2, default2) is False

os.environ[var1] = "true"
os.environ[var2] = "true"
assert get_bool_env(var1, default1) is True
assert get_bool_env(var2, default2) is True

os.environ[var1] = "some crap"
try:
    assert get_bool_env(var1, default1) is False
except Exception as ex:
    assert str(ex) == "Invalid boolean config: some crap"

os.environ[var1] = '"{}"'
try:
    assert get_bool_env(var1, default1) is False
except Exception as ae:
    assert isinstance(ae, AssertionError)
del os.environ[var1], os.environ[var2]
del var1, var2, default1, default2

# ======== end sanity tests for get_bool_env ==================

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "BDGD9HDJD0)JDJDJ%$DJDHADQGJPZLPQAF^&%HJ"
    "BKOPWHLEKQPHPTUSFDVWOQWPAKIEOMBZXAPYTSZ%",
)


DEBUG = get_bool_env("DEBUG", True)

allowed_hosts = os.getenv(
    "ALLOWED_HOSTS",
    ".localhost",
)

ALLOWED_HOSTS = allowed_hosts.split(",")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'todo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'todo.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        "NAME": os.getenv("DB_NAME", "tododb"),
        "USER": os.getenv("DB_USER", "app"),
        "PASSWORD": os.getenv("DB_PASS", "app"),
        "HOST": os.getenv("DB_HOST", "127.0.0.1"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
