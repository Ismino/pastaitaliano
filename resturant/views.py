from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Table, Reservation, STATUS_CHOICES
from .forms import BookingForm, ReservationSearchForm 

@login_required
def make_reservation(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.status = STATUS_CHOICES[0][0]
            booking.save()
            messages.success(request, 'Booking successfully made.')
            return redirect('view_booking')
        else:
            messages.error(request, 'Chosen booking is not available.')
    form = BookingForm()
    context = {
        'form': form
        }
    return render(request, 'restaurant/make_reservation.html', context)

@login_required
def search_reservation(request):
    form = ReservationSearchForm(request.GET)
    reservations = Booking.objects.filter(user=request.user)

    



