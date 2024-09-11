from django.shortcuts import render, redirect
from .models import Room, Booking, Waitlist
from .forms import BookingForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils.timezone import now

def home(request):
    # You can pass context here if needed
    return render(request, 'booking/home.html')

def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            # Calculate total price (room + package + services)
            total_price = booking.room.price_per_night
            if booking.package:
                total_price += booking.package.price
            for service in booking.services.all():
                total_price += service.price
            booking.total_price = total_price
            booking.save()

            # Send email confirmation
            send_mail(
                'Booking Confirmation',
                f'Your booking for {booking.room.room_number} is confirmed!',
                settings.DEFAULT_FROM_EMAIL,
                [request.user.email]
            )
            messages.success(request, 'Booking confirmed!')

            return redirect('booking_confirmation')
    else:
        form = BookingForm()

    return render(request, 'booking/booking_form.html', {'form': form})

def booking_confirmation(request):
    return render(request, 'booking/confirmation.html')\
        
def join_waitlist(request, room_id):
    room = Room.objects.get(id=room_id)
    if not room.is_available:
        waitlist_entry, created = Waitlist.objects.get_or_create(user=request.user, room=room)
        messages.success(request, 'You have been added to the waitlist.')
    else:
        messages.error(request, 'Room is available. No need for waitlist.')
    return redirect('booking')

