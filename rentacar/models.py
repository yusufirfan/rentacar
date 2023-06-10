from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    def __str__(self):
        return f''

class Car(models.Model):
    plate_number = models.CharField(max_length=256)
    brand = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    year = models.SmallIntegerField()
    gear = models.CharField(max_length=256,null=True,blank=True)
    reservation = models.ForeignKey(Reservation,on_delete=models.SET_NULL,null=True,blank=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.plate_number} - {self.brand}'

    