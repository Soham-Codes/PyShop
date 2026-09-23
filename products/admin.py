from django.contrib import admin
from .models import Product, Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','discount') # tuple


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock') # tuple 


admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)


