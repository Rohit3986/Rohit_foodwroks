from django.db import models


# Create your models here.

#this table will store foods data will be display in menu
class foodrecord(models.Model):
    item_name=models.CharField(max_length=30)
    item_type=models.CharField(max_length=30)
    item_price=models.CharField(max_length=30)
    stock_available=models.CharField(max_length=30)

#this table will store user booked order records
class orderrecord(models.Model):
    item_name=models.CharField(max_length=30)
    ordered_qty=models.CharField(max_length=30)
    item_price=models.CharField(max_length=30)
    order_id=models.CharField(max_length=30)
    total_payable=models.CharField(max_length=30)

    