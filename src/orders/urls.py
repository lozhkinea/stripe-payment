from django.urls import path

from orders.views import BuyAPIView, ItemAPIView

app_name = 'orders'

urlpatterns = [
    path('buy/<int:id>/', BuyAPIView.as_view(), name='buy'),
    path('item/<int:id>/', ItemAPIView.as_view(), name='item'),
]
