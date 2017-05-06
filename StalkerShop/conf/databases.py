# -*- coding: utf-8 -*-
u"""
Configuración de conexiones a bases de datos del proyecto. Los valores que
puedan cambiar entre los entornos de Desarrollo, QA y Producción están en el
archivo secrets.py, así como claves o valores sensibles que no se deban subir a
GitHub.

:Authors:
    - Gabriel Ruiz

:Last Modification:
    - 06.05.2017
"""
import traceback
try:
    from StalkerShop.conf import secrets
    CONFIG = secrets.CONFIG
except ImportError:
    CONFIG = {}
except Exception:
    traceback.print_exc()
    CONFIG = {}

# Databases
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DB_CONFIG = CONFIG.get('databases', {})
DB_DEFAULT = DB_CONFIG.get('default', {})

# La configuracion por defecto es para testing
DATABASES = {
    'default': {
        'ENGINE': DB_DEFAULT.get('engine', 'django.db.backends.sqlite3'),
        'NAME': DB_DEFAULT.get('name', 'stalker.db'),
        'USER': DB_DEFAULT.get('user', ''),
        'PASSWORD': DB_DEFAULT.get('password', ''),
        'HOST': DB_DEFAULT.get('host', ''),
        'PORT': DB_DEFAULT.get('port', '3306'),
        'TEST': {
            'NAME': 'test_stalkershop',
            'USER': 'testuser',
            'password': 'testpassword'
        }
    },
}
