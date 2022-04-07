from cgi import print_exception
from django.contrib.auth.models import User
from django.db import models

from apps.products.models import Product



class Order(models.Model):
    class Status(models.Model):
        CHOICES = (
            (0, 'New'),
            (1, 'Framed'),
            (2, 'Canceled'),
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    agreement = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(max_length=100)
    status_of_order = models.IntegerField(default=0, choices=Status.CHOICES)

    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return self.first_name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.IntegerField(default=1)
    amount = models.IntegerField(default=1)
    discount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'{self.id}'
    