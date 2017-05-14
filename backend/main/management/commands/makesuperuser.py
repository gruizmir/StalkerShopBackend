# -*- coding: utf-8 -*-
u"""
Comando para crear un superusuario con valores por defecto.
"""
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="gabriel").exists():
            User.objects.create_superuser("gabriel",
                "gabriel.ruiz.miranda@gmail.com",
                settings.SUPERUSER_PASSWORD)
