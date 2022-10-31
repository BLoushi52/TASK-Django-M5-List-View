from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from .serializers import FlightsListSerializer

class FlightsListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightsListSerializer