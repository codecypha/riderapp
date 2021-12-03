
from django.db import models


# Create your models here.
class Order(models.Model):
    initiator = models.CharField(max_length=150, blank=True)
    pickup = models.CharField(max_length=150)
    dropoff = models.CharField(max_length=150)
    itemName = models.CharField(max_length=150)
    quantity = models.CharField(max_length=150)
    note = models.CharField(max_length=250, blank=True)
    reciever_name = models.CharField(max_length=150)
    recievers_phone = models.CharField(max_length=150)
    stan=models.DateTimeField(auto_now_add=True)
    status =models.CharField(max_length=10,default= 'inactive')
    orderid =models.CharField(max_length=250, blank=True, unique=True)
    entry_date=models.DateField(auto_now_add=True)
    update_date=models.DateField(auto_now=True)


    def __str__(self):
        return self.initiator
    
    class Meta:
        db_table = 'customer_order'