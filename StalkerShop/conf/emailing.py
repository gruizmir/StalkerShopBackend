# -*- coding: utf-8 -*-
u"""
Configuración del backend de emailing del proyecto. Los valores que puedan
cambiar entre los entornos de Desarrollo, QA y Producción están en el archivo
secrets.py, así como claves o valores sensibles que no se deban subir a GitHub.

:Authors:
    - Gabriel Ruiz

:Last Modification:
    - 29.05.2017
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

EMAIL_CONFIGS = CONFIG.get('email', {}).get('smtp', {})
EMAIL_USE_TLS = EMAIL_CONFIGS.get('use_tls', True)
EMAIL_HOST = EMAIL_CONFIGS.get('host', '')
EMAIL_HOST_USER = EMAIL_CONFIGS.get('user', '')
EMAIL_HOST_PASSWORD = EMAIL_CONFIGS.get('password', '')
EMAIL_PORT = EMAIL_CONFIGS.get('port', 587)
EMAIL_PROVIDERS = CONFIG.get('email', {}).get('providers', {})
DEFAULT_FROM_EMAIL = u''
DEFAULT_FROM_NAME = u''
CONTACT_EMAIL = ''

EMAIL_SUBJECT_PREFIX = u'[DESTACAME]'
