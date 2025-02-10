from django.shortcuts import render, redirect
from .models import Order
from .sberpay import create_payment
import uuid


def create_order(request):
    order_id = str(uuid.uuid4())[:8]
    order = Order.objects.create(order_id=order_id, amount=100.00)

    payment_url = create_payment(order.amount, "http://localhost:8000/payment_success/")

    if payment_url:
        return redirect(payment_url)

    return render(request, "error.html", {"message": "Ошибка создания платежа"})


def payment_success(request):
    return render(request, "success.html")
