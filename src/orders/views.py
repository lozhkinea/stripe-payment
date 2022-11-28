from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from orders import services


class BuyAPIView(View):
    def get(self, request, id):
        session_id = services.get_checkout_session_id_for_item(id)
        return JsonResponse(session_id)


class BuyOrderAPIView(View):
    def get(self, request, id):
        session_id = services.get_checkout_session_id_for_order(id)
        return JsonResponse(session_id)


class ItemAPIView(View):
    def get(self, request, id):
        template = 'orders/checkout.html'
        context = {
            'item': services.get_item(id),
            'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY,
        }
        return render(request, template, context)


class OrderAPIView(View):
    def get(self, request, id):
        template = 'orders/checkout.html'
        context = {
            'order': services.get_order(id),
            'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY,
        }
        return render(request, template, context)
