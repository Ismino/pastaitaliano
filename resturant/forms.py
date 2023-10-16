# imports needed for the forms
from tempus_dominus.widgets import DateTimePicker
from django import forms
from .models import Reservation
from datetime import datetime
from django.utils import timezone

# Form that handels reservations and sets the fields, also a widget for the date & time


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'user', 'reservation_datetime']

        widgets = {
            'reservation_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean_reservation_datetime(self):
        reservation_datetime = self.cleaned_data.get('reservation_datetime')
        if reservation_datetime < timezone.now():
            raise forms.ValidationError("Reservation date and time cannot be in the past.")
        return reservation_datetime

# Form that handels the reservations search form


class ReservationSearchForm(forms.Form):
    reservation_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    user_name = forms.CharField(max_length=100, required=False)