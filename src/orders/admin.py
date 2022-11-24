from django.contrib import admin

from orders.models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')


admin.site.register(Item, ItemAdmin)
