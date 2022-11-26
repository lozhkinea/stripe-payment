import os

import stripe
from django.shortcuts import get_object_or_404
from django.urls import reverse

from orders.models import Item, Order

HOST = 'http://localhost:8000'
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


def get_price_data(item, amount):
    """Создает данные для API Stripe по одному Item."""
    return {
        'price_data': {
            'currency': 'usd',
            'product_data': {
                'name': item.name,
                'description': item.description,
            },
            'unit_amount_decimal': item.price * 100,
        },
        'quantity': amount,
        'adjustable_quantity': {'enabled': True},
    }


def create_checkout_session_for_item(id):
    """Создает Session в Stripe для Item."""
    item = get_object_or_404(Item, id=id)
    url = HOST + reverse('orders:item', kwargs={'id': id})
    return stripe.checkout.Session.create(
        cancel_url=url,
        mode='payment',
        success_url=url,
        line_items=[get_price_data(item, 1)],
    )


def create_checkout_session_for_order(id):
    """Создает Session в Stripe для Order."""
    order = get_object_or_404(Order, id=id)
    url = HOST + reverse('orders:order', kwargs={'id': id})
    return stripe.checkout.Session.create(
        cancel_url=url,
        mode='payment',
        success_url=url,
        line_items=[
            get_price_data(order_item.item, order_item.amount)
            for order_item in order.order_items.all()
        ],
        discounts=[
            {
                'coupon': order.discount.coupon,
            }
        ],
    )


def get_item(id):
    """Возвращает Item из базы данных."""
    return get_object_or_404(Item, id=id)


def get_order(id):
    """Возвращает Order из базы данных."""
    return get_object_or_404(Order, id=id)
