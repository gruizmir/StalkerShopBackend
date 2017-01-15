# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from main.api import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', ProductViewSet, base_name="product")

urlpatterns = []
urlpatterns += [
    url(r'^', include(router.urls)),
]
    
