# Generated by Django 4.2.7 on 2023-11-18 07:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_rooms_booking', '0007_meetingroom_booking_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinghistory',
            name='booking_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 18, 12, 31, 30, 122593)),
        ),
    ]
