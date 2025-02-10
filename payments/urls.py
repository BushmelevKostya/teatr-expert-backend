from django.urls import path
from .views import create_order, payment_success

urlpatterns = [
    path("pay/", create_order, name="create_order"),
    path("payment_success/", payment_success, name="payment_success"),
]
