from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Responder(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=250, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    product_id = models.CharField(max_length=75)
    product_name = models.CharField(max_length=200)
    quantity = models.IntegerField(null=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Re-stocked', 'Re-stocked'),
    )
    supplier = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    cost = models.FloatField(null=True)
    product = models.ForeignKey(Inventory, null=True, on_delete=models.SET_NULL)
    responder = models.ForeignKey(Responder, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.product.product_name


