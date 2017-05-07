# -*- coding: utf-8 -*-
u"""
Configuración de conexiones a bases de datos del proyecto. Los valores que
puedan cambiar entre los entornos de Desarrollo, QA y Producción están en el
archivo secrets.py, así como claves o valores sensibles que no se deban subir a
GitHub.

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

# Databases
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# La configuracion por defecto es para testing
DATABASES = {
    'default': {
        'ENGINE': CONFIG.get('RDS_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': CONFIG.get('RDS_DB_NAME', 'stalker.db'),
        'USER': CONFIG.get('RDS_USERNAME', ''),
        'PASSWORD': CONFIG.get('RDS_PASSWORD', ''),
        'HOST': CONFIG.get('RDS_HOSTNAME', ''),
        'PORT': CONFIG.get('RDS_PORT', '3306'),
        'TEST': {
            'NAME': 'test_stalkershop',
            'USER': 'testuser',
            'password': 'testpassword'
        }
    },
}
