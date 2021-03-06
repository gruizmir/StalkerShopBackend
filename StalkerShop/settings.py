"""
Django settings for StalkerShop project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import os
import pymysql
import traceback
from datetime import timedelta

try:
    from StalkerShop.conf import secrets
    CONFIG = secrets.CONFIG
except ImportError:
    CONFIG = {}
except Exception:
    traceback.print_exc()
    CONFIG = {}

from StalkerShop.conf.calculations import *
from StalkerShop.conf.databases import *
from StalkerShop.conf.emailing import *
from StalkerShop.conf.files import *
from StalkerShop.conf.security import *


pymysql.install_as_MySQLdb()

SITE_ID = 1

# ADMINISTRATION SETTINGS
ADMIN_CONFIGS = CONFIG.get('administration', {})
ADMINS = ADMIN_CONFIGS.get('admins', ())

DEBUG = CONFIG.get('debug', True)
ALLOWED_HOSTS = CONFIG.get('allowed_hosts', [])


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

INTERNAL_IPS = ('127.0.0.1',)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'corsheaders',
    'main.apps.MainConfig'
]

MIDDLEWARE = [
    # 'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'StalkerShop.urls'
WSGI_APPLICATION = 'StalkerShop.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.csrf',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'StalkerShop.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

DEFAULT_TIME_FORMAT = "%d/%m/%Y"
DEFAULT_DATE_FORMAT = "%d/%m/%Y"

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'UNICODE_JSON': False,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': timedelta(hours=1),
    'JWT_ALLOW_REFRESH': True,
}
