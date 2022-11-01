from .models import Booking, Flight
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import FlightsListSerializer, BookingsListSerializer, BookingDetailSerializer

class FlightsListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightsListSerializer

class BookingsListView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingsListSerializer

class DetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'