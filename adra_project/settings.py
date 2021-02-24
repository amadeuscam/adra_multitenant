import os
from sentry_sdk.integrations.django import DjangoIntegration
import sentry_sdk
import environ
from celery.schedules import crontab

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(env('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']

# django-allauth config
SESSION_COOKIE_AGE = 86400

TOKEN_KEY_USER = str(env('TOKEN_USER'))
# Application definition

SHARED_APPS = (
    'tenant_schemas',
    'shared',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'django_filters',
    # 'crispy_forms',
    # 'rest_framework',
    # 'rest_framework.authtoken',

)

TENANT_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'adra',
    'allauth',
    'allauth.account',
    'django_filters',
    'crispy_forms',
    'rest_framework',
    'rest_framework.authtoken',

)

INSTALLED_APPS = [
    'tenant_schemas',
    'shared',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django_filters',
    'crispy_forms',
    'rest_framework',
    'rest_framework.authtoken',
    'tenant_schemas_celery',
    'adra',

]
SITE_ID = 1

MIDDLEWARE = [
    'tenant_schemas.middleware.TenantMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware'
]

ROOT_URLCONF = 'adra_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'adra_project.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

# Database

NAME_DB = "adra_torrejon_new"
USER_DB = str(str(env('mysql_user')))
PASSWORD_DB = str(str(env('mysql_password')))

DATABASE_ROUTERS = (
    'tenant_schemas.routers.TenantSyncRouter',
)

if DEBUG:
    SITE_DOAMIN = 'http://localhost:8000/'
    DATABASES = {
        'default': {
            'ENGINE': 'tenant_schemas.postgresql_backend',
            'NAME': 'adra_new',
            'USER': 'postgres',
            'PASSWORD': 'masina',
            'HOST': "192.168.0.211",
            'PORT': 5432,
            'CHARSET': 'UTF8'
        }
    }
else:
    SITE_DOAMIN = 'http://164.90.211.207/'
    DATABASES = {
        'default': {
            'ENGINE': 'tenant_schemas.postgresql_backend',
            'NAME': 'adra_new',
            'USER': 'postgres',
            'PASSWORD': 'masina',
            'HOST': "192.168.0.211",
            'PORT': 5432,
            'CHARSET': 'UTF8'
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",

]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es-eu'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# AUTH_USER_MODEL = "users.CustomUser"
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL = 'adra:persona-home'
ACCOUNT_LOGOUT_REDIRECT = 'adra:persona-home'  # new
# LOGOUT_REDIRECT_URL = "/"

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

STATIC_URL = '/static/'
# local static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
# Production static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_FROM_EMAIL = 'luciancati@adratorrejon.es'

EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
SENDGRID_API_KEY = str(env('SENDGRID_API_KEY'))
SENDGRID_SANDBOX_MODE_IN_DEBUG = False

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400  # 1 day in seconds
# ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/logout/'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_SIGNUP_FORM_CLASS = 'adra.forms.SignupForm'
ACCOUNT_ADAPTER = 'adra.views.CustomAllauthAdapter'

# chache page
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': 'cache_table',
#     }
# }
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 0  # una semana
CACHE_MIDDLEWARE_KEY_PREFIX = ''

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
CORS_ORIGIN_ALLOW_ALL = True

sentry_sdk.init(
    dsn="https://c65bac75837247648592312de561bab2@sentry.io/1515282",
    integrations=[DjangoIntegration()]
)

CELERY_BROKER_URL = 'amqp://localhost'
# CELERY_BROKER_URL = 'amqp://guest@localhost//'
# BROKER_URL = 'redis://localhost:6379'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'

TELEGRAM_TOKEN_KEY = str(env('telegram_token'))

PLATFORM_NAME = ""

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING'
    }

}

TENANT_MODEL = 'shared.Delegaciones'
DEFAULT_FILE_STORAGE = 'tenant_schemas.storage.TenantFileSystemStorage'


# CELERY_TASK_TENANT_CACHE_SECONDS = os.environ.get("TASK_TENANT_CACHE_SECONDS", 0)
# CELERYD_PREFETCH_MULTIPLIER = 1
# CELERY_ACKS_LATE = True
