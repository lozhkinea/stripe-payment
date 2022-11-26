import stripe
from django.contrib import admin

from orders.models import Discount, Item, Order, OrderItem


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'discount')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'item')
    list_filter = ('order',)


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('coupon_id', 'percent_off', 'duration')

    def save_model(self, request, obj, form, change):
        if not obj.coupon_id:
            obj.coupon_id = stripe.Coupon.create(
                percent_off=obj.percent_off,
                duration=obj.duration,
            ).id
        obj.save()

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            stripe.Coupon(id=obj.coupon_id).delete()
        queryset.delete()

    def delete_model(self, request, obj):
        stripe.Coupon(id=obj.coupon_id).delete()
        obj.delete()


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Discount, DiscountAdmin)
