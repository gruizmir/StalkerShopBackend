# -*- coding: utf-8 -*-
import traceback
import os 

try:
    import secrets
    CONFIG = secrets.CONFIG
except:
    traceback.print_exc()
    CONFIG = {}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
LOCAL_DEPLOY = CONFIG.get('local_deploy', True)

AWS_CONFIGS = CONFIG.get('aws', {})
AWS_REGION = AWS_CONFIGS.get('region', 'us-west-2')
AWS_ACCESS_KEY_ID = AWS_CONFIGS.get('access_key_id', '')
AWS_SECRET_ACCESS_KEY = AWS_CONFIGS.get('secret_access_key', '')
AWS_SES_REGION_NAME = 'us-west-2'
AWS_SES_REGION_ENDPOINT = 'email.us-west-2.amazonaws.com'

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
    AWS_STORAGE_BUCKET_NAME = AWS_CONFIGS.get('static_bucket_name', '')
    AWS_MEDIA_BUCKET_NAME = AWS_CONFIGS.get('media_bucket_name', '')

    # Tell django-storages that when coming up with the URL for an item in S3
    # storage, keep it simple - just use this domain plus the path. (If this
    # isn't set, things get complicated).
    # This controls how the `static` template tag from `staticfiles` gets
    # expanded, if you're using it. We also use it in the next setting.
    AWS_S3_CUSTOM_DOMAIN = AWS_CONFIGS.get('static_service_domain',
                            '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME)

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
