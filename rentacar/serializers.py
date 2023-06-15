from rest_framework import serializers
from .models import Car,Reservation

class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
