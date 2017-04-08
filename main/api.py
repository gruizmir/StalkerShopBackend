# -*- coding: utf-8 -*-
from rest_framework import viewsets
from main.models import Product
from main.serializers import ProductSerializer
from rest_framework.authentication import TokenAuthentication, \
    BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter,\
    FilterSet, CharFilter
from django_filters import DateTimeFromToRangeFilter, NumberFilter


class ProductFilter(FilterSet):
    min_price = NumberFilter(name="price_3", lookup_expr='gte')
    max_price = NumberFilter(name="price_3", lookup_expr='lte')
    min_discount = NumberFilter(name="real_discount",
        lookup_expr='gte')
    max_discount = NumberFilter(name="real_discount", 
        lookup_expr='lte')
    created = DateTimeFromToRangeFilter()
    name = CharFilter()

    o = OrderingFilter(
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
        serializer.save()
