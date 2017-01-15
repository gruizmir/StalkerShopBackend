# -*- coding: utf-8 -*-
import traceback
try:
    import secrets
    CONFIG = secrets.CONFIG
except:
    traceback.print_exc()
    CONFIG = {}


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CONFIG.get('secret_key')

## SEGURIDAD Y OTRAS HIERBAS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ()
CORS_ORIGIN_REGEX_WHITELIST = ()
CORS_URLS_REGEX = '^.*$'
CORS_EXPOSE_HEADERS = ()
CORS_ALLOW_CREDENTIALS = True
CORS_PREFLIGHT_MAX_AGE = 86400

SESSION_COOKIE_SECURE = CONFIG.get('secure_cookies', False)
CSRF_COOKIE_SECURE = CONFIG.get('secure_cookies', False)
CSRF_COOKIE_HTTPONLY = True

SECRET_KEY = CONFIG.get('secret_key', False) 


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/es/1.9/ref/settings/#secure-browser-xss-filter

SECURE_CONTENT_TYPE_NOSNIFF = True
# https://docs.djangoproject.com/es/1.9/ref/settings/#secure-content-type-nosniff

SECURE_SSL_REDIRECT = True
# https://docs.djangoproject.com/es/1.9/ref/settings/#secure-ssl-redirect


# TODO: Agregar estas configuraciones

# DISALLOWED_USER_AGENTS = []
# https://docs.djangoproject.com/es/1.9/ref/settings/#disallowed-user-agents

# FIXTURE_DIRS
# https://docs.djangoproject.com/es/1.9/ref/settings/#fixture-dirs

# TODO: Revisar X-Content-Type-Options: nosniff en AWS S3
