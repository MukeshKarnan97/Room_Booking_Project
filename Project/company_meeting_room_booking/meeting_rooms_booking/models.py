# models.py


from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

from django.forms import ValidationError


def validate_future_date(value):
    if value < timezone.now():
        raise ValidationError("Booking date must be the current or a future date.")



class MeetingRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_available = models.BooleanField(default=False)
    current_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    booking_date = models.DateTimeField(validators=[validate_future_date])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        # Update the updated_at field before saving
        self.updated_at = timezone.now().date()
        super().save(*args, **kwargs)

        BookingHistory.objects.create(
            room_name=str(self),
            user_name=str(self.current_user),
            booking_date=self.booking_date
        )


class BookingHistory(models.Model):
    room_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    booking_date = models.DateTimeField(default=timezone.now().date())

    def __str__(self):
        return f"{self.user_name} booked {self.room_name} on {self.booking_date}"