""" from rest_framework import serializers
from .models import MeetingRoom

class MeetingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRoom
        fields = ('id', 'name', 'is_booked', 'booked_by')
 """


# serializers.py

from rest_framework import serializers
from .models import MeetingRoom

class MeetingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingRoom
        fields = ['id', 'name', 'created_at']
