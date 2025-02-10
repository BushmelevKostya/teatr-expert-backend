from django.db import models


class Order(models.Model):
    order_id = models.CharField(max_length=50, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="created")

    def __str__(self):
        return f"Order {self.order_id}: {self.status}"
