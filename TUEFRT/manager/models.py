from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Responder(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=250, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create a updateInventory model. See how that would work in our db.

class Inventory(models.Model):
    product_id = models.CharField(max_length=75)
    product_name = models.CharField(max_length=200)
    quantity = models.IntegerField(null=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.product_name
# NOTE: Add another field "type" is the order of type 'msk', 'respiratory' etc...

# NOTE: Will be utilized in the dashboard.
class UpdatedInventory(models.Model):
    update_id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    responder = models.ManyToManyField(Responder)
    QuantityUsed = models.IntegerField(default=1,
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )

    def __str__(self):
        return f"update {self.update_id} ({self.product}) on {self.date_created.date()}"

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


