from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Booking

@shared_task
def send_reminder():
    bookings = Booking.objects.filter(check_in__gt=timezone.now(), check_in__lte=timezone.now() + timezone.timedelta(days=2))
    for booking in bookings:
        send_mail(
            'Upcoming Booking Reminder',
            f'Reminder for your booking: {booking.room}',
            'your_email@example.com',
            [booking.user.email]
        )
