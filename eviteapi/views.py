# Create your views here.
from rest_framework import viewsets

from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('name')
    serializer_class = EventSerializer
