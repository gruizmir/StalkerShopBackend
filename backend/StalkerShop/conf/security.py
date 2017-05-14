# -*- coding: utf-8 -*-
u"""
Configuración de seguridad del proyecto. Los valores que puedan cambiar entre
los entornos de Desarrollo, QA y Producción están en el archivo secrets.py, así
como claves o valores sensibles que no se deban subir a GitHub.

:Authors:
    - Gabriel Ruiz

:Last Modification:
    - 29.05.2017
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

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CONFIG.get('SECRET_KEY',
    'ba8)rw3n!fro(qsi0p_(*(g%m5q+a3!q4l5(!)((#j$m823+e8')

# SEGURIDAD Y OTRAS HIERBAS
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = ('http://localhost:8100', 'localhost:8100',)
CORS_ORIGIN_REGEX_WHITELIST = ()
CORS_URLS_REGEX = '^.*$'
CORS_EXPOSE_HEADERS = ()
CORS_ALLOW_CREDENTIALS = True
CORS_PREFLIGHT_MAX_AGE = 86400
CORS_ALLOW_METHODS = (
    'GET',
    'OPTIONS',
    'POST',
)


SESSION_COOKIE_SECURE = CONFIG.get('SECURE_COOKIES', False)
CSRF_COOKIE_SECURE = CONFIG.get('SECURE_COOKIES', False)
CSRF_COOKIE_HTTPONLY = True

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.NumericPasswordValidator',
    },
]

SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/es/1.9/ref/settings/#secure-browser-xss-filter

SECURE_CONTENT_TYPE_NOSNIFF = True
# https://docs.djangoproject.com/es/1.9/ref/settings/#secure-content-type-nosniff

SECURE_SSL_REDIRECT = True
# https://docs.djangoproject.com/es/1.9/ref/settings/#secure-ssl-redirect
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

# DISALLOWED_USER_AGENTS = ['python-requests']
# https://docs.djangoproject.com/es/1.9/ref/settings/#disallowed-user-agents

# TODO: Agregar estas configuraciones
# FIXTURE_DIRS
# https://docs.djangoproject.com/es/1.9/ref/settings/#fixture-dirs

# TODO: Revisar X-Content-Type-Options: nosniff en AWS S3

# Este valor se debe borrar de las variables de entorno en
# Elastic Beanstalk después de su primera ejecución.
SUPERUSER_PASSWORD = CONFIG.get('SUPERUSER_PASSWORD', '')