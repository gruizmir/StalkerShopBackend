# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from main.models import Product
from django.dispatch import receiver


@receiver(post_save, sender=Product)
def product_post_save_handler(sender, **kwargs):
    u"""
    Verifica si el producto existe en la misma tienda y tiene un precio
    que haya disminuido en más de un 80% respecto al anterior.
    """
    product = kwargs['instance']
    created = kwargs['created']
    if not created:
        return

    if product.has_good_discount():
        # TODO: Enviar notificacion PUSH
        # send_notification(product)
        print("good discount")
        # pass
    similar_product = Product.objects.filter(sku=product.sku)\
        .exclude(id=product.id).last()
    if (similar_product and
            product.has_good_discount(comparative=similar_product)):
        # TODO: Enviar notificacion PUSH
        # send_notification(product)
        pass
