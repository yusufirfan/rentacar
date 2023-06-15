from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.exceptions import ValidationError

class FixModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Car(FixModel):
    plate_number = models.CharField(max_length=24, unique=True)
    brand = models.CharField(max_length=24)
    model = models.CharField(max_length=24)
    year = models.PositiveIntegerField()

    GEAR_CHOICES=[
        (0,'Manual'),
        (1,'Auto'),
    ]

    gear = models.BooleanField(choices=GEAR_CHOICES)
    rent_per_day = models.CharField(max_length=24)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.plate_number} - {self.brand}'
    
class Reservation(FixModel):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.user_id} / {self.start_date} - {self.end_date}'

    def save(self, *args, **kwargs):
        if self.end_date<date.today():
            raise ValidationError("You can't select a date in the past.")
        else:
            super().save(*args, **kwargs)