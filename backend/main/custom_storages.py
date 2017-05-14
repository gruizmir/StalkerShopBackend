# -*- coding: utf-8 -*-
u"""
Clases para enviar los archivos estáticos y archivos media de usuario a AWS S3.
Utilizan la librería 'boto' y 'django-storages' para funcionar.
"""
from django.conf import settings
from storages.backends.s3boto import S3BotoStorage


class StaticStorage(S3BotoStorage):
    u"""
    Archivos estáticos. Solo importa el nombre del bucket para los archivos
    estáticos.
    """
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME or None


class MediaStorage(S3BotoStorage):
    u"""
    Archivos de usuario. El atributo 'file_overwrite' en False deja los
    archivos subidos como no editables por defecto.
    """
    bucket_name = settings.AWS_MEDIA_BUCKET_NAME or None
    custom_domain = settings.AWS_S3_MEDIA_DOMAIN
    file_overwrite = False

    def path(self, name):
        return self._normalize_name(name)
