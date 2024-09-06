from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_room, name='book_room'),
    path('confirmation/', views.booking_confirmation, name='booking_confirmation'),
]
