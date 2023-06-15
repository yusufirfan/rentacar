from rest_framework import serializers
from .models import Car,Reservation

class FixSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(required=False, read_only=True)

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        return super().create(validated_data)

class CarSerializers(FixSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class ReservationSerializers(FixSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
