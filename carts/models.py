from django.db import models
from django.conf import settings

from decimal import Decimal

from apps.products.models import Product


class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.created_at} - {self.updated_at}'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def __str__(self):
        return f'{self.user} - {self.item} - {self.quantity} - {self.created_at} - {self.updated_at}'


class DeliveryCost(models.Model):
    status = models.CharField(max_length=7,
                              choices=(('Active', 'active'), ('Passive', 'passive')),
                              default="passive",
                              null=False)
    cost_per_delivery = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    cost_per_product = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    fixed_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f'{self.status}-'
                f'{self.cost_per_delivery}-'
                f'{self.cost_per_product}-'
                f'{self.fixed_cost}-'
                f'{self.created_at}-{self.updated_at}')
                                                