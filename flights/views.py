from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from .serializers import FlightsListSerializer, BookingsListSerializer

class FlightsListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightsListSerializer

class BookingsListView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingsListSerializer