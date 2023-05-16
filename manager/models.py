from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    medicine_id=models.IntegerField(null=False)
    medicine_name = models.CharField(null=False,max_length=100)
    quantity=models.IntegerField(default=1)
    purchase_date = models.DateTimeField(auto_now_add=True)
    purchase_amount = models.DecimalField(max_digits=10, decimal_places=2)
    expiry_date = models.DateField(default=datetime.now().date() + timedelta(days=365))



class Inventory(models.Model):
    product_id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField(default=0)
    medicine_name = models.CharField(max_length=100)
    expiry_date=models.DateField(null=True)
    objects = models.Manager()



class Orders(models.Model):
    cut_name = models.CharField(max_length=100, null=False)


class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=100, null=False)
    quantity = models.PositiveIntegerField(null=False)
    prescription = models.TextField(null=True)
