from django import forms
from .models import Reservation
from datetime import datetime

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'user', 'reservation_datetime']

    def clean_reservation_datetime(self):
        reservation_datetime = self.cleaned_data.get('reservation_datetime')
        if reservation_datetime < timezone.now():
            raise forms.ValidationError("Reservation date and time cannot be in the past.")
        return reservation_datetime

class ReservationSearchForm(forms.Form):
    user_name = forms.CharField(max_length=100, required=False)
    reservation_date = forms.DateField(required=False)

    def clean_reservation_date(self):
        reservation_date = self.cleaned_data.get('reservation_date')
        if reservation_date and reservation_date < timezone.now().date():
            raise forms.ValidationError("Reservation date cannot be in the past.")
        return reservation_date