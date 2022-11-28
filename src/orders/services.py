import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.urls import reverse

from orders.models import Item, Order

stripe.api_key = settings.STRIPE_SECRET_KEY


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


def get_checkout_session_id_for_item(id):
    """Создает Session в Stripe для Item и возвращает id."""
    item = get_item(id)
    url = settings.DOMAIN_URL + reverse('orders:item', kwargs={'id': id})
    try:
        session = stripe.checkout.Session.create(
            cancel_url=url,
            mode='payment',
            success_url=url,
            line_items=[get_price_data(item, 1)],
        )
        return {'session_id': session.id}
    except Exception as e:
        return {'error': str(e)}


def get_checkout_session_id_for_order(id):
    """Создает Session в Stripe для Order и возвращает id."""
    order = get_order(id)
    items = order.order_items.all()
    url = settings.DOMAIN_URL + reverse('orders:order', kwargs={'id': id})
    try:
        session = stripe.checkout.Session.create(
            cancel_url=url,
            mode='payment',
            success_url=url,
            line_items=[
                get_price_data(item.item, item.amount) for item in items
            ],
            discounts=[
                {
                    'coupon': order.discount.coupon_id,
                }
            ],
        )
        return {'session_id': session.id}
    except Exception as e:
        return {'error': str(e)}


def get_item(id):
    """Возвращает Item из базы данных."""
    return get_object_or_404(Item, id=id)


def get_order(id):
    """Возвращает Order из базы данных."""
    return get_object_or_404(Order, id=id)
