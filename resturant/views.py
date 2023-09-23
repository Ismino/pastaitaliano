from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Table, Reservation, STATUS_CHOICES
from .forms import ReservationForm, ReservationSearchForm 
from django.contrib import messages

def home_page(request):
    return render(request, 'index.html')

def contact_page(request):
    return render(request, 'contact.html')

def menu_page(request):
    return render(request, 'menu.html')

@login_required
def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.status = 1
            reservation.save()
            messages.success(request, 'Reservation successfully made.')
            return redirect('view_reservation')
        else:
            messages.error(request, 'Chosen reservation is not available.')
    form = ReservationForm()
    context = {
        'form': form
        }
    return render(request, 'make_reservation.html', context)

@login_required

def search_reservation(request):
    if request.method == 'POST':
        form = ReservationSearchForm(request.POST)
        if form.is_valid():
            reservation_date = form.cleaned_data['reservation_date']
            user = request.user

            # Search for reservations
            reservations = Reservation.objects.filter(
                user=request.user,
                reservation_datetime__date=reservation_date
            )

            context = {
                'form': form,
                'reservations': reservations
            }

            return render(request, 'search_reservations.html', context)
    else:
        form = ReservationSearchForm()

    context = {
        'form': form
    }

    return render(request, 'search_reservations.html', context)

@login_required
def view_reservation(request):
    reservation = Reservation.objects.filter(user=request.user)
    context = {
        'reservation': reservation
        } 
    return render(request, 'view_reservation.html', context)

@login_required
def edit_or_delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    
    if request.method == "POST":
        # Check if a 'delete' parameter is present in the POST data
        if 'delete' in request.POST:
            # Handle reservation deletion
            if reservation.delete():
                messages.success(request, 'Your reservation has been deleted.')
        else:
            # Handle reservation editing
            form = ReservationForm(request.POST, instance=reservation)
            if form.is_valid():
                reservation = form.save()
                reservation.user = request.user
                reservation.save()
                messages.success(request, 'Your reservation has been updated.')

        return redirect('view_reservations')

    form = ReservationForm(instance=reservation)
    context = {
        'form': form
    }
    return render(request, 'edit_or_delete_reservation.html', context)

           



