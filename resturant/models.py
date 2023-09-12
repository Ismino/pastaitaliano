from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

# Define choices for reservation status
# Inspired by CodeInstitute models for Django Blog app
STATUS_CHOICES = (
    (0,'Undefined'),
    (1, 'Confirmed'),
    (2, 'Cancelled'),
)

# Class for the resturant name to be used in relations to the other Classes
class Restaurant(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Class for the Table that handels the seats and info of the table 
class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    seats = models.IntegerField()
    min_people = models.IntegerField()
    max_people = models.IntegerField()

    def __str__(self):
        return f"Table at {self.restaurant.name} - Seats: {self.seats}"

#Class fot the reservaton info and a validation error if the reservation is done in the past
class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_datetime = models.DateTimeField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    # Inspiered method from https://github.com/renatalantos/booking-system/blob/main/restaurant/models.py  
    def ValidationHandler(self):
        if self.reservation_datetime < timezone.now():
            raise ValidationError("Reservation date and time cannot be in the past.")

    def __str__(self):
        return f"Reservation for {self.user.username} at {self.table.name}"

    def is_confirmed(self):
        return self.status == 1

    def is_cancelled(self):
        return self.status == 2
