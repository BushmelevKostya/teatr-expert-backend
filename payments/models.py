from django.db import models


class OrderStatus(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=10, choices=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')], unique=True)

    def __str__(self):
        return self.name


class SeatStatus(models.Model):
    name = models.CharField(max_length=20, choices=[('available', 'Available'), ('reserved', 'Reserved'), ('sold', 'Sold')], unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.CharField(max_length=50, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_DEFAULT, default=None)
    count_seats = models.IntegerField()

    def __str__(self):
        return f"Order {self.order_id}: {self.status}, Amount: {self.amount}, Seats: {self.count_seats}"


class Sale(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="sales")
    percents = models.IntegerField()
    count_seats = models.IntegerField()

    def __str__(self):
        return f"Sale {self.id}: Order {self.order.order_id}, Discount: {self.percents}%"


class SeatClass(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    row = models.IntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f"SeatClass {self.id}: Row {self.row}, Region {self.region}, Price {self.amount}"


class Seat(models.Model):
    seat_class = models.ForeignKey(SeatClass, on_delete=models.CASCADE, related_name="seats")
    status = models.ForeignKey(SeatStatus, on_delete=models.SET_DEFAULT, default=None)

    def __str__(self):
        return f"Seat {self.id}: Class {self.seat_class.id}, Status {self.status}"
