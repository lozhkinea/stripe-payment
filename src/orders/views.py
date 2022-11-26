from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

import orders.services as svc


class BuyAPIView(View):
    def get(self, request, id):
        session = svc.create_checkout_session_for_item(id)
        return JsonResponse({'session_id': session.id})


class BuyOrderAPIView(View):
    def get(self, request, id):
        session = svc.create_checkout_session_for_order(id)
        return JsonResponse({'session_id': session.id})


class ItemAPIView(View):
    def get(self, request, id):
        template = 'orders/checkout_item.html'
        context = {
            'item': svc.get_item(id),
            'pkey': svc.STRIPE_PUBLIC_KEY,
        }
        return render(request, template, context)


class OrderAPIView(View):
    def get(self, request, id):
        template = 'orders/checkout_order.html'
        context = {
            'order': svc.get_order(id),
            'pkey': svc.STRIPE_PUBLIC_KEY,
        }
        return render(request, template, context)
