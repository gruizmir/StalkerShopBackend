# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        import main.signals
        # TODO: Cambiar a Log
        print('Loaded {}'.format(main.signals))