from os import getenv

import stripe
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View

from orders.models import Item, Order

stripe.api_key = getenv('STRIPE_SECRET_KEY')


class BuyAPIView(View):
    def get(self, request, id):
        item = get_object_or_404(Item, id=id)
        url = 'http://localhost:8000' + reverse(
            'orders:item', kwargs={'id': id}
        )
        session = stripe.checkout.Session.create(
            cancel_url=url,
            mode='payment',
            success_url=url,
            line_items=[get_price_data(item)],
        )
        return JsonResponse({'session_id': session.id})


class BuyOrderAPIView(View):
    def get(self, request, id):
        order = get_object_or_404(Order, id=id)
        url = 'http://localhost:8000' + reverse(
            'orders:order', kwargs={'id': id}
        )
        session = stripe.checkout.Session.create(
            cancel_url=url,
            mode='payment',
            success_url=url,
            line_items=[
                get_price_data(item) for item in order.order_items.all()
            ],
        )
        return JsonResponse({'session_id': session.id})


def get_price_data(order_item):
    return {
        'price_data': {
            'currency': 'usd',
            'product_data': {
                'name': order_item.item.name,
                'description': order_item.item.description,
            },
            'unit_amount_decimal': order_item.item.price * 100,
        },
        'quantity': order_item.amount,
        'adjustable_quantity': {'enabled': True},
    }


class ItemAPIView(View):
    def get(self, request, id):
        item = get_object_or_404(Item, id=id)
        template = 'orders/checkout_item.html'
        context = {
            'item': item,
            'pkey': getenv('STRIPE_PUBLIC_KEY'),
        }
        return render(request, template, context)


class OrderAPIView(View):
    def get(self, request, id):
        order = get_object_or_404(Order, id=id)
        template = 'orders/checkout_order.html'
        context = {
            'order': order,
            'order_items': order.order_items.all(),
            'pkey': getenv('STRIPE_PUBLIC_KEY'),
        }
        return render(request, template, context)
