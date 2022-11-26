from django.urls import path

from orders.views import BuyAPIView, ItemAPIView, OrderAPIView, BuyOrderAPIView

app_name = 'orders'

urlpatterns = [
    path('buy/<int:id>/', BuyAPIView.as_view(), name='buy'),
    path('item/<int:id>/', ItemAPIView.as_view(), name='item'),
    path('buy_order/<int:id>/', BuyOrderAPIView.as_view(), name='buy_order'),
    path('order/<int:id>/', OrderAPIView.as_view(), name='order'),
]
