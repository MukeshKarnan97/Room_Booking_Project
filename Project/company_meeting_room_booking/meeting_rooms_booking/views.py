# views.py

import json
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import MeetingRoom
from .serializers import MeetingRoomSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework import generics, permissions

class MeetingRoomList(generics.ListAPIView):
    queryset = MeetingRoom.objects.filter(is_available=True)
    serializer_class = MeetingRoomSerializer



class BookMeetingRoom(generics.UpdateAPIView):
    queryset = MeetingRoom.objects.all()
    serializer_class = MeetingRoomSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        meeting_room_id = self.kwargs.get('meeting_room_id')

        emp_name = request.data['emp_name']

        try:
            user = User.objects.get(username=emp_name)
        except User.DoesNotExist:
            return Response({"error": f"User with ID {emp_name} not found"}, status=status.HTTP_404_NOT_FOUND)
        

        if MeetingRoom.objects.filter(current_user=user).exists():
            return Response({"error": f"User {user.username} has already booked a room"}, status=status.HTTP_400_BAD_REQUEST)



        try:
            instance = MeetingRoom.objects.get(pk=meeting_room_id, is_available=True)
        except MeetingRoom.DoesNotExist:
            return Response({"error": "Meeting room already booked"}, status=status.HTTP_400_BAD_REQUEST)

        instance.is_available = False
        instance.booking_date = request.data['booking_date']
        instance.current_user = user
        instance.save()

        return Response("Successfully Room Booked", status=status.HTTP_201_CREATED)
    


@csrf_exempt
def generate_token(request):
    auth_detail = json.loads(request.body)
    username = auth_detail.get('username')
    password = auth_detail.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        token = Token.objects.get_or_create(user=user)
        token = token[0].key
    else:
        token = None

    return JsonResponse({'token': token})