
from django.urls import path
from .views import MeetingRoomList, BookMeetingRoom, generate_token

urlpatterns = [
    path('meeting-rooms/', MeetingRoomList.as_view(), name='meeting-room-list'),
    path('book-meeting-room/<int:meeting_room_id>/', BookMeetingRoom.as_view(), name='book-meeting-room'),
    path('get-token/', generate_token, name='get_token'),
]
