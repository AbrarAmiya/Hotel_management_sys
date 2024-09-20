from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Room, Booking
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from decimal import Decimal
from django.shortcuts import get_object_or_404
from .models import *
    
# 1234@push
def home_view(request):
    if 'user_id' in request.session:
        return HttpResponse(f"Welcome, User {request.session['user_id']}!")
    return render(request, 'accounts/home.html')

def view_rooms(request):
    rooms = Room.objects.all()
    for room in rooms:
        room.offer_price = room.price_per_night * Decimal('1.2')  # Calculate offer price

    return render(request, 'accounts/view_rooms.html', {'rooms': rooms})


def feedback_view(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        room_id = request.POST.get('room')
        room = Room.objects.get(id=room_id)
        
        Feedback.objects.create(room=room, rating=rating, comment=comment)
        return redirect('feedback_success')

    rooms = Room.objects.all()
    return render(request, 'accounts/feedback.html', {'rooms': rooms})


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exists!')
            return redirect('register')

        # Create new user
        user = User(username=username)
        user.set_password(password)
        user.save()

        # Log the user in directly after registration (optional)
        new_user = authenticate(username=username, password=password)
        if new_user is not None:
            login(request, new_user)
            return redirect('home')

        # Redirect to login if you want users to login manually after registration
        # return redirect('login')
    
    return render(request, 'accounts/signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after login
        else:
            messages.error(request, 'Invalid email or password')

    return render(request, 'accounts\login.html')

@login_required
def book_room(request):
    rooms = Room.objects.filter(is_available=True)  # Show only available rooms
    if request.method == 'POST':
        room_id = request.POST.get('room')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')

        try:
            room = Room.objects.get(id=room_id)
            check_in_date = timezone.datetime.strptime(check_in, '%Y-%m-%d').date()
            check_out_date = timezone.datetime.strptime(check_out, '%Y-%m-%d').date()
            
            if check_in_date >= check_out_date:
                messages.error(request, 'Check-out date must be after check-in date.')
                return redirect('book_room')

            total_days = (check_out_date - check_in_date).days
            total_price = room.price_per_night * total_days

            # Create the booking
            booking = Booking.objects.create(
                user=request.user,
                room=room,
                check_in=check_in_date,
                check_out=check_out_date,
                total_price=total_price
            )

            # Mark room as unavailable after booking
            room.is_available = False
            room.save()

            messages.success(request, 'Booking successful!')
            return redirect('booking_confirmation', booking_id=booking.id)  # Redirect to booking confirmation

        except Room.DoesNotExist:
            messages.error(request, 'Room not found.')
            return redirect('book_room')

    return render(request, 'accounts/booking_form.html', {'rooms': rooms})

def logout_view(request):
    logout(request)
    return render(request, 'accounts/logout.html')

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'accounts/booking_confirmation.html', {'booking': booking})