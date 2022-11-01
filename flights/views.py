from .models import Booking, Flight
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .serializers import FlightsListSerializer, BookingsListSerializer, BookingDetailSerializer, BookingUpdateSerializer

class FlightsListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightsListSerializer

class BookingsListView(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingsListSerializer

class BookingDetailView(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'

class BookingUpdateView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'

class BookingDestroyView(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer  #Using Detail Serializer as we dont need specific one.
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'