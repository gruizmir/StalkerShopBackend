# -*- coding: utf-8 -*-
u"""
Configuración de valores estáticos usados para cálculos en el proyecto. Los
valores que puedan cambiar entre los entornos de Desarrollo, QA y Producción
están en el archivo secrets.py, así como claves o valores sensibles que no se
deban subir a GitHub.

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

GOOD_DISCOUNT = CONFIG.get('GOOD_DISCOUNT', 70)
HOLY_DISCOUNT = CONFIG.get('HOLY_DISCOUNT', 90)
HOLY_FUCKING_SHIT_DISCOUNT = CONFIG.get('HOLY_FUCKING_SHIT_DISCOUNT', 99)
