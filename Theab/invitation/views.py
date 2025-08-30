from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Event, Guest
from .serializers import EventSerializer, GuestSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['get'])
    def guests(self, request, pk=None):
        event = self.get_object()
        guests = event.guests.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)
    
class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get_queryset(self):
        user = self.request.user
        return Guest.objects.filter(event__user=user)

    def perform_create(self, serializer):
        event_id = self.request.data.get('event')
        event = Event.objects.get(id=event_id, user=self.request.user)
        serializer.save(event=event)


