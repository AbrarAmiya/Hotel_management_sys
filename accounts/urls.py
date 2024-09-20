from django.urls import path
from .views import register_view, login_view, logout_view, home_view, feedback_view, view_rooms, book_room, booking_confirmation

urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('book-room/', book_room, name='book_room'),
    path('view_rooms', view_rooms, name='view_rooms'), 
    path('feedback/', feedback_view, name='feedback_form'),
    path('booking_confirmation/<int:booking_id>/', booking_confirmation, name='booking_confirmation'),  # Add this line
]
