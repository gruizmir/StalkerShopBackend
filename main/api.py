# -*- coding: utf-8 -*-
import django_filters
from rest_framework import viewsets
from main.models import Product
from main.serializers import ProductSerializer
from rest_framework.authentication import TokenAuthentication, \
    BasicAuthentication
from rest_framework.filters import DjangoFilterBackend, OrderingFilter,\
    SearchFilter, FilterSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.decorators import detail_route
# from rest_framework.renderers import StaticHTMLRenderer


class ProductFilter(FilterSet):
    min_price = django_filters.NumberFilter(name="price_3", lookup_expr='gte')
    max_price = django_filters.NumberFilter(name="price_3", lookup_expr='lte')
    min_discount = django_filters.NumberFilter(name="real_discount",
        lookup_expr='gte')
    max_discount = django_filters.NumberFilter(name="real_discount", 
        lookup_expr='lte')
    created = django_filters.DateTimeFromToRangeFilter()

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
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    filter_class = ProductFilter
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering_fields = ('store', 'price_3', 'real_discount', 'updated')
    search_fields = ('name', )

    # @detail_route(renderer_classes=[StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     producto = self.get_object()
    #     return Response(product.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
