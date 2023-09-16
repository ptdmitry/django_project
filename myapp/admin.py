from django.contrib import admin
from .models import Client, Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'count', 'added_date']
    ordering = ['added_date']
    list_filter = ['added_date', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю описания продукта (description).'
    readonly_fields = ['added_date']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'registered_date']
    ordering = ['registered_date']
    list_filter = ['registered_date', 'phone']
    search_fields = ['phone']
    search_help_text = 'Поиск по полю номера телефона (phone).'
    readonly_fields = ['name', 'email', 'phone', 'address', 'registered_date']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'amount', 'registered_order_date']
    ordering = ['registered_order_date']
    list_filter = ['registered_order_date', 'product']
    search_fields = ['product']
    search_help_text = 'Поиск по полю названия продукта (product).'
    readonly_fields = ['client', 'product', 'amount', 'registered_order_date']


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
