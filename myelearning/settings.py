"""
Django settings for myelearning project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from decouple import config
from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', 'dummy_secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', 'True', cast=bool)

ALLOWED_HOSTS = ['*','elearningdominators.azurewebsites.net']


# Application definition

INSTALLED_APPS = [
    'courses',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.admindocs',
    'crispy_forms',
    'students',
    'embed_video',
    'rest_framework',
    'storages',
    'widget_tweaks',
    'corsheaders',
    'taggit',
    'taggit_serializer',
    'termsandconditions',
]

MIDDLEWARE = [
    'opencensus.ext.django.middleware.OpencensusMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'students.middleware.SessionTimeoutMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    # 'termsandconditions.middleware.TermsAndConditionsRedirectMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

# if DEBUG == False:
    # MIDDLEWARE += ('courses.middleware.SubdomainCourseMiddleware')


ROOT_URLCONF = 'myelearning.urls'

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

WSGI_APPLICATION = 'myelearning.wsgi.application'

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'elearning',
#         'USER': 'postgres',
#         'PASSWORD': '1234',
#         'PORT': '5432',
#         'HOST': 'localhost'
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'elearning',
        'USER': 'elearning_admin@elearningserver',
        'PASSWORD': 'Dominators123',
        'PORT': '5432',
        'HOST': 'elearningserver.postgres.database.azure.com'
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Custom auth

AUTH_USER_MODEL = 'students.User'
LOGIN_REDIRECT_URL = reverse_lazy('classroom')
LOGIN_URL = reverse_lazy('login')
LOGOOUT_URL = reverse_lazy('logout')
LOGOUT_REDIRECT_URL = reverse_lazy('course_list')


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'students.authentication.EmailAuthBackend',
]


# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
CACHE_MIDDLEWARE_SECONDS = 60 * 15  # 15 minutes
CACHE_MIDDLEWARE_KEY_PREFIX = 'el'

# DRF
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer',
    )
}

# Mailer
DEFAULT_FROM_EMAIL = config('ADMIN_EMAIL', 'ayushkmr397@gmail.com')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Session
SESSION_EXPIRE_SECONDS = 18000  # 5 hours
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True

DEVELOPER_KEY = config('DEVELOPER_API_KEY', 'developer_key_here')

# corsheaders
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = (
    'https://myelearning.herokuapp.com',
    'http://localhost:8080',
    'http://localhost:8100',
    'http://localhost:8000',
    'http://localhost:3000',
    'https://pwa-myelearning.netlify.app',
    'http://localhost',
)

CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'DELETE',
)

# Task async
CELERY_BROKER_URL = config('REDIS_URL', 'redis://localhost:6379/0', cast=str)
CELERY_RESULT_BACKEND = config('REDIS_URL', 'redis://localhost:6379/0', cast=str)

# Terms & Conditions settings

DEFAULT_TERMS_SLUG = "site-terms"
ACCEPT_TERMS_PATH = "/terms/accept/"
TERMS_EXCLUDE_URL_PREFIX_LIST = {"/admin", "/terms"}
TERMS_EXCLUDE_URL_LIST = {"/", "/course/termsrequired/", "/accounts/login/", "/students/register/student/", "/students/register/teacher/"}
TERMS_CACHE_SECONDS = 60 * 15
TERMS_EXCLUDE_USERS_WITH_PERM = "auth.can_skip_t&c"
TERMS_IP_HEADER_NAME = "REMOTE_ADDR"
TERMS_STORE_IP_ADDRESS = True
TERMS_BASE_TEMPLATE = 'base.html'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# For monitoring
OPENCENSUS = {
    'TRACE': {
        'SAMPLER': 'opencensus.trace.samplers.ProbabilitySampler(rate=1)',
        'EXPORTER': '''opencensus.ext.azure.trace_exporter.AzureExporter(
            connection_string="InstrumentationKey=e7b43f56-96e8-41ed-9182-b6ee2e5a8272;IngestionEndpoint=https://eastus-8.in.applicationinsights.azure.com/;LiveEndpoint=https://eastus.livediagnostics.monitor.azure.com/"
        )''',
    }
}

DEFAULT_FILE_STORAGE = 'myelearning.custom_azure.AzureMediaStorage'
STATICFILES_STORAGE = 'myelearning.custom_azure.AzureStaticStorage'

STATIC_LOCATION = "static"
MEDIA_LOCATION = "media"

AZURE_ACCOUNT_NAME = "elearningstorageacc"
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'