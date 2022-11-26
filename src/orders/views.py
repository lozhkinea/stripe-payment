from os import getenv

import stripe
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View

from orders.models import Item

stripe.api_key = getenv('STRIPE_API_KEY')


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
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.name,
                            'description': item.description,
                        },
                        'unit_amount_decimal': item.price * 100,
                    },
                    'quantity': 1,
                    'adjustable_quantity': {'enabled': True},
                }
            ],
        )
        return JsonResponse({'session_id': session.id})


class ItemAPIView(View):
    def get(self, request, id):
        item = get_object_or_404(Item, id=id)
        template = 'orders/checkout.html'
        context = {'item': item}
        return render(request, template, context)
