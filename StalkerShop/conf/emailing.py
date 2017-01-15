# -*- coding: utf-8 -*-
import traceback
try:
    import secrets
    CONFIG = secrets.CONFIG
except:
    traceback.print_exc()
    CONFIG = {}

# Communication systems
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
COMMUNICATIONS_EMAIL_SUBJECT_PREFIX = u'[DESTACAME]'
