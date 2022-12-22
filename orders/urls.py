from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import OrderCreateView, OrderDetailView, OrderListView, SuccessView

app_name = 'orders'

urlpatterns = [
    path('order-create/', login_required(OrderCreateView.as_view()), name='order_create'),
    path('', login_required(OrderListView.as_view()), name='orders_list'),
    path('order/<int:pk>/', login_required(OrderDetailView.as_view()), name='order'),
    path('order-success/', login_required(SuccessView.as_view()), name='order_success'),
]
