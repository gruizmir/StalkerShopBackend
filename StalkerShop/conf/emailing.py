# -*- coding: utf-8 -*-
u"""
Configuración del backend de emailing del proyecto. Los valores que puedan
cambiar entre los entornos de Desarrollo, QA y Producción están en el archivo
secrets.py, así como claves o valores sensibles que no se deban subir a GitHub.

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

EMAIL_USE_TLS = CONFIG.get('EMAIL_USE_TLS', True)
EMAIL_HOST = CONFIG.get('EMAIL_HOST', '')
EMAIL_HOST_USER = CONFIG.get('EMAIL_USER', '')
EMAIL_HOST_PASSWORD = CONFIG.get('EMAIL_PASSWORD', '')
EMAIL_PORT = CONFIG.get('EMAIL_PORT', 587)

DEFAULT_FROM_EMAIL = CONFIG.get('EMAIL_DEFAULT_FROM', '')
DEFAULT_FROM_NAME = CONFIG.get('EMAIL_DEFAULT_NAME', '')
EMAIL_SUBJECT_PREFIX = u'[StalkerShop]'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
