# -*- coding: utf-8 -*-
u"""
Configuración de almacenamiento de archivos estáticos y de archivos subidos por
usuarios en el proyecto. Los valores que puedan cambiar entre los entornos de
Desarrollo, QA y Producción están en el archivo secrets.py, así como claves o
valores sensibles que no se deban subir a GitHub.

:Authors:
    - Gabriel Ruiz

:Last Modification:
    - 07.05.2017
"""
import os
import traceback

try:
    from StalkerShop.conf import secrets
    CONFIG = secrets.CONFIG
except ImportError:
    CONFIG = os.environ
except Exception:
    traceback.print_exc()
    CONFIG = {}


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
LOCAL_DEPLOY = CONFIG.get('LOCAL_DEPLOY', True)
DEBUG = CONFIG.get('DEBUG', True)

AWS_REGION = CONFIG.get('AWS_DEFAULT_REGION', 'us-west-2')
AWS_ACCESS_KEY_ID = CONFIG.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = CONFIG.get('AWS_SECRET_ACCESS_KEY', '')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
if LOCAL_DEPLOY:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
else:
    # Serving static files from AWS S3.
    # Boto: Include this headers in the response when serving from S3
    AWS_HEADERS = {
        'Expires': '7d',
        'Cache-Control': 'max-age=604800',
    }
    AWS_STORAGE_BUCKET_NAME = CONFIG.get('AWS_STATIC_BUCKET_NAME', '')
    AWS_MEDIA_BUCKET_NAME = CONFIG.get('AWS_MEDIA_BUCKET_NAME', '')

    # Tell django-storages that when coming up with the URL for an item in S3
    # storage, keep it simple - just use this domain plus the path. (If this
    # isn't set, things get complicated).
    # This controls how the `static` template tag from `staticfiles` gets
    # expanded, if you're using it. We also use it in the next setting.
    AWS_S3_CUSTOM_DOMAIN = CONFIG.get('AWS_S3_CUSTOM_DOMAIN') or \
                            '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    # This is used by the `static` template tag from `static`, if you're
    # using that. Or if anything else refers directly to STATIC_URL. So it's
    # safest to always set it.
    STATIC_ROOT = 'staticfiles'

    # Tell the staticfiles app to use S3Boto storage when writing the collected
    # static files (when you run `collectstatic`).
    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'main.custom_storages.StaticStorage'
    STATIC_URL = "https://%s/" % (AWS_S3_CUSTOM_DOMAIN)
    STATIC_DIRECTORY = '/static/'

    AWS_S3_MEDIA_DOMAIN = '%s.s3.amazonaws.com' % AWS_MEDIA_BUCKET_NAME
    MEDIA_URL = "https://%s/" % (AWS_S3_MEDIA_DOMAIN)
    MEDIA_ROOT = MEDIA_URL
    DEFAULT_FILE_STORAGE = 'main.custom_storages.MediaStorage'

MEDIA_TEMP = 'temp'


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

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)
