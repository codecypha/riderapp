
from django.db import models


# Create your models here.
class Driver(models.Model):
    firstName = models.CharField(max_length=150)
    lastName = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    driver_email = models.EmailField(blank=True)
    phone_num = models.CharField(max_length=20)
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(
        max_length=15,
        choices= gender_choices,
        default = 'Male'
    )
    
    licence_num = models.CharField(max_length=150)
    profile_pic = models.ImageField(blank=True)
    bike_num = models.CharField(max_length=150, blank=True)
    entry_date=models.DateField(auto_now_add=True)
    update_date=models.DateField(auto_now=True)


    def __str__(self):
        return self.phone_num
    
    class Meta:
        db_table = 'driver_info'

