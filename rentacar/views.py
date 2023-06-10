from .serializers import Car,CarSerializers,Reservation,ReservationSerializers

from rest_framework.generics import ListCreateAPIView,ListAPIView
from rest_framework.permissions  import IsAdminUser
from rest_framework.response import Response
from rest_framework import status

class CarListCreateView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers
    # permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        if self.request.user.is_superuser is True:
            return super().create(request, *args, **kwargs)
        data = {
            'message': 'You are not authorized to create!'
        }
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)



class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers

    def get_queryset(self):
        id = self.kwargs["pk"]
        return Car.objects.filter(id=id)