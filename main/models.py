# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

class Product(models.Model):
    u"""
    Modelo que representa un producto de una tienda,
    para almacenar.

    Attributes
    ----------
    name : CharField
        Nombre del producto, según la descripción de la lista de 
        productos de la tienda.
    url : URLField
        URL del detalle del producto.
    sku : CharField
        SKU - Identificador del producto dentro de la tienda de retail.
    store : CharField
        Tienda en la que el producto está a la venta.
    price_1 : IntegerField
        Precio 'normal' del producto, según lo publica la tienda.
    price_2 : IntegerField
        Precio 'internet' u 'oferta' del producto, según lo publica la tienda.
    price_3 : IntegerField
        Precio 'con tarjeta X' del producto, según lo publica la tienda. Puede 
        corresponder al mismo valor de price_2, si no existe oferta con tarjeta.

    """
    STORE_OPTIONS = (
        ('falabella', _('Falabella')),
        ('ripley', _('Ripley')),
        ('paris', _('Paris')),
        ('sodimac', _('Sodimac')),
        ('easy', _('Easy')),
        ('hites', _('Hites')),
        ('abcdin', _('Abcdin')),
        ('pcfactory', _('PcFactory')),
    )
    name = models.CharField(_('Name'), max_length=200, null=False, blank=False)
    url = models.URLField(_('URL'), max_length=300, null=False, blank=False)
    sku = models.CharField(_('SKU'), max_length=30, null=True, blank=True)
    store = models.CharField(_('Store'), max_length=200, choices=STORE_OPTIONS,
        null=False, blank=False)
    price_1 = models.IntegerField(_('Price_1'), null=False, blank=False)
    price_2 = models.IntegerField(_('Price_2'), null=False, blank=False)
    price_3 = models.IntegerField(_('Price_3'), null=False, blank=False)
    published_discount = models.IntegerField(_('PublishedDiscount'), 
        null=True, blank=True)
    calc_discount = models.IntegerField(_('RealDiscount'), 
        null=True, blank=True)
    image_url = models.URLField(_('ImageURL'), max_length=300, null=False, 
        blank=False)
    description = models.TextField(_('Description'), null=True, blank=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True)
    created = models.DateTimeField(_('Created'), auto_now_add=True, 
        editable=False)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        app_label = 'main'

    def __unicode__(self):
        return self.name

    def has_good_discount(self, comparative=None):
        if comparative:
            compare_price = min(comparative.get_prices())
            current_price = min(self.get_prices())
            self.calc_discount = \
                100 * (compare_price - current_price) / compare_price
        else:
            prices = self.get_prices()
            min_price = min(prices)
            max_price = max(prices)
            self.published_discount = 100 * (max_price - min_price) / max_price
            self.calc_discount = self.published_discount
        self.save()
        return self.calc_discount >= settings.GOOD_DISCOUNT

    def get_prices(self):
        prices = list(filter(None, [self.price_3, self.price_2, self.price_1]))
        return prices
