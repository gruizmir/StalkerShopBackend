# -*- coding: utf-8 -*-
from rest_framework import serializers
from main.models import Product
from drf_queryfields import QueryFieldsMixin


class ProductSerializer(QueryFieldsMixin, serializers.ModelSerializer):
    u"""
    Serializador de modelo Product. Por el momento, no incluye 
    métodos adicionales ni serializadores a FKs.
    """

    class Meta:
        model = Product
        exclude = ('created', )
