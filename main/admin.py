# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from main.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'store', 'calc_discount', 'price_3', 'get_link')
    list_filter = ('store', 'updated')
    save_on_top = True

    def get_link(self, obj):
        link = "<a href=\"%s\" target=\"_blank\">Ver</a>"
        link = link % obj.url
        return link

    get_link.allow_tags = True
    get_link.short_description = _("Link")
