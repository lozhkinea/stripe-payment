from django.contrib import admin

from orders.models import Item, Order, OrderItem


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'item')
    list_filter = ('order',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Order)
admin.site.register(OrderItem, OrderItemAdmin)
