from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.utils import timezone

# Define choices for reservation status
STATUS_CHOICES = (
    (0, 'Pending'),
    (1, 'Confirmed'),
    (2, 'Cancelled'),
)

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    # Add other restaurant information fields here

    def __str__(self):
        return self.name

class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    seats = models.IntegerField()
    min_people = models.IntegerField()
    max_people = models.IntegerField()

    def __str__(self):
        return f"Table at {self.restaurant.name} - Seats: {self.seats}"

class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_datetime = models.DateTimeField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def clean(self):
        if self.reservation_datetime < timezone.now():
            raise ValidationError("Reservation date and time cannot be in the past.")

    def __str__(self):
        return f"Reservation for {self.customer.username} at {self.table.restaurant.name}"

    def is_pending(self):
        return self.status == 0

    def is_confirmed(self):
        return self.status == 1

    def is_cancelled(self):
        return self.status == 2
