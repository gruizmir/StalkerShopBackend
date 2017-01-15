# -*- coding: utf-8 -*-
import traceback
try:
    import secrets
    CONFIG = secrets.CONFIG
except:
    traceback.print_exc()
    CONFIG = {}

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DB_CONFIG = CONFIG.get('databases', {})
if 'test' in sys.argv and 'test' in DB_CONFIG.keys():
    DB_DEFAULT = DB_CONFIG.get('test', {})
else:
    DB_DEFAULT = DB_CONFIG.get('default', {})

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_DEFAULT.get('name', ''),
        'USER': DB_DEFAULT.get('user', ''),
        'PASSWORD': DB_DEFAULT.get('password', ''),
        'HOST': DB_DEFAULT.get('host', ''),
        'PORT': DB_DEFAULT.get('port', '3306')
    },
}
