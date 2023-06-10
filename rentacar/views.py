from .serializers import Car,CarSerializers,Reservation,ReservationSerializers
from rest_framework.generics import ListCreateAPIView,ListAPIView
from rest_framework.permissions  import IsAdminUser

class CarListCreateView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers
    permission_classes = [IsAdminUser]

class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers

    def get_queryset(self):
        id = self.kwargs["pk"]
        return Car.objects.filter(id=id)