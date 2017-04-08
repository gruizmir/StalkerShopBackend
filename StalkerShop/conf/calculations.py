# -*- coding: utf-8 -*-
import traceback
try:
    from StalkerShop.conf import secrets
    CONFIG = secrets.CONFIG
except:
    traceback.print_exc()
    CONFIG = {}

GOOD_DISCOUNT = CONFIG.get('discounts', {}).get('good', 70)
HOLY_DISCOUNT = CONFIG.get('discounts', {}).get('holy', 90)
HOLY_FUCKING_SHIT_DISCOUNT = CONFIG.get('discounts', {}).get('holy_shit', 99)
