# -*- coding: utf-8 -*-
u"""
Vistas de la API Rest de StalkerShop, referentes a los productos que se
van a almacenar y comparar.

:Authors:
    - Gabriel Ruiz

:Last Modification:
    - 06.05.2017
"""
from rest_framework import viewsets
from main.models import Product
from main.serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter,\
    FilterSet, CharFilter
from django_filters import DateTimeFromToRangeFilter, NumberFilter


class ProductFilter(FilterSet):
    u"""
    Filtros para la búsqueda de productos en la API. Oculta los nombres
    reales de algunos campos para facilitar la aplicación.

    Attributes
    ----------
    min_price : django_filters.NumberFilter
        Mínimo precio de los productos a buscar. Compara contra el valor
        de 'price_3' del producto.
    max_price : django_filters.NumberFilter
        Máximo precio de los productos a buscar. Compara contra el valor
        de 'price_3' del producto.
    min_discount : django_filters.NumberFilter
        Mínimo descuento aplicado en los producots a buscar. Compara
        contra el valor de 'real_discount' del producto.
    max_discount : django_filters.NumberFilter
        Máximo descuento aplicado en los producots a buscar. Compara
        contra el valor de 'real_discount' del producto.
    created : django_filters.DateTimeFromToRangeFilter
        Filtro por rango de fecha. Se aplica de la siguiente forma:
            - created_0: Fecha mínima de creación del producto en DB.
            - created_1: Fecha máxima de creación del producto en DB.
    name : django_filters.rest_framework.CharFilter
        Filtro por nombre del producto. Ocupa una comparación similar a
        'LIKE *value*' en la consulta.
    order : django_filters.rest_framework.OrderingFilter
        Filtro para aplicar ordenamiento en la salida de los datos.
        Los valores posibles son 'store', 'price_3', 'real_discount'
        y 'updated'

    :Authors:
        - Gabriel Ruiz

    :Last Modification:
        - 06.05.2017
    """
    min_price = NumberFilter(name="price_3", lookup_expr='gte')
    max_price = NumberFilter(name="price_3", lookup_expr='lte')
    min_discount = NumberFilter(name="real_discount", lookup_expr='gte')
    max_discount = NumberFilter(name="real_discount", lookup_expr='lte')
    created = DateTimeFromToRangeFilter()
    name = CharFilter()

    order = OrderingFilter(
        fields=(
            ('store', 'store'),
            ('price_3', 'price_3'),
            ('real_discount', 'real_discount'),
            ('updated', 'updated'),
        ),
    )

    class Meta:
        model = Product
        fields = ['store', 'updated', 'min_price', 'max_price',
                  'min_discount', 'max_discount']


class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_class = ProductFilter
    filter_backends = (DjangoFilterBackend, )

    def perform_create(self, serializer):
        u"""
        Guarda los datos del serializador en BD.

        :Authors:
            - Gabriel Ruiz

        :Last Modification:
            - 06.05.2017
        """
        serializer.save()
