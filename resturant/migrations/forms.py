from django import forms
from .models import Reservation
from datetime import datetime

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_date_and_time', 'user_name']

    def process_reservation(self, user):
        reservation = self.save(commit=False)
        reservation.user = user
        reservation.status = Booking.STATUS_CHOICES[0][0]

        # Set the reservation date and time to the current date and time
        now = datetime.now()
        reservation.reservation_date_and_time = now

        reservation.save()
        return reservation


class ReservationSearchForm(forms.ModelForm):
    reservation_date_and_time = forms.DateField(label='Date and time for reservation', required=False, widget=forms.DateInput(attrs={'type': 'date'}))


