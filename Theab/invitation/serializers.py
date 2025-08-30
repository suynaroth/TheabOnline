from rest_framework import serializers
from .models import Event, Guest

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'user', 'name', 'date', 'location', 'description', 'create_at']

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['id', 'event', 'name', 'unique_slug']

