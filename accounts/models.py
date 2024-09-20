from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    feedback_score = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    feedback_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Room {self.room_number} - {self.room_type}"

    class Meta:
        db_table = 'room'  # Set your custom table name here

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking by {self.user.username} for Room {self.room.room_number}"

    class Meta:
        db_table = 'booking'  # Set your custom table name here
        
class Feedback(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    user_id = models.IntegerField(default=1)  # Set default value here
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'feedback'  # This tells Django to use the 'feedback' table in the database

    def __str__(self):
        return f"Feedback by {self.user} for room {self.room}"