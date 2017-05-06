# -*- coding: utf-8 -*-
u"""
Casos de Test para probar la API de StalkerShop.

:Authors:
    - Gabriel Ruiz

:Last Modification:
    - 06.05.2017
"""
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import Product
from rest_framework import status
from rest_framework.test import APITestCase

# TODO: Test post con token correcto
# TODO: Test get con sesion corecta
# TODO: Test get con token correcto
# TODO: Test get fallido
# TODO: Test de obtencion de JWT
# TODO: Test de renovacion de JWT


class ProductsTests(APITestCase):

    def setUp(self):
        u"""
        Crea un usuario y un producto para iniciar el test.
        """
        user = User.objects.create(username='testuser', is_active=True)
        user.set_password('testpassword')
        Product.objects.create(name="Samsung Smart TV",
            url="https://mitienda.com",
            price_1=300000,
            price_3=100000,
            store='MiTienda',
            sku='232131231L')

    def test_create_product(self):
        u"""
        Verifica que se puede crear un producto correctamente, con
        un usuario autenticado.
        """
        url = reverse('product-list')
        data = {
            'name': 'MOTO G 4TA',
            'url': 'http://www.falabella.com/falabella-cl/product/5155721/'
                   'LED-55-UN55KU6000-4K-Ultra-HD-Smart-TV',
            'price_1': 209990,
            'price_2': 179990,
            'price_3': 109990,
            'store': 'ripley',
            'sku': '2000358595041P'
        }
        user = User.objects.get(username='testuser')
        self.client.force_authenticate(user=user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(Product.objects.last().name, 'MOTO G 4TA')

    def test_create_product_failure(self):
        u"""
        Verifica que la creación de un producto no sea posible para
        un usuario no autenticado o no autorizado.
        """
        url = reverse('product-list')
        data = {
            'name': 'MOTO G 4TA',
            'url': 'http://www.falabella.com',
            'price_1': 200000,
            'price_2': 150000,
            'price_3': 100000,
            'store': 'ripley',
            'sku': '2000358595041P'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Product.objects.count(), 1)
