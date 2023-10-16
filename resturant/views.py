# imports needed for the views
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Table, Reservation, STATUS_CHOICES
from .forms import ReservationForm, ReservationSearchForm 
from django.contrib import messages
from django.urls import reverse

# view for homepage 


def home_page(request):
    return render(request, 'index.html')

# view for contact page


def contact_page(request):
    return render(request, 'contact.html')

# view for menu page 


def menu_page(request):
    return render(request, 'menu.html')

# view for reservation page for loged in users


@login_required
def make_reservation(request):
    if request.method == 'POST':
        # Create a ReservationForm instance with the POST data
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Create a reservation object but don't save it to the database yet
            reservation = form.save(commit=False)
            # Set the user for this reservation to the currently logged in user
            reservation.user = request.user
            reservation.status = 1
            # Save the reservation to the database
            reservation.save()
            messages.success(request, 'Reservation successfully made.')
            return redirect('view_reservation')
        else:
            messages.error(request, 'Chosen reservation is not available.')
            # If the request is not a POST request, create an empty ReservationForm
    form = ReservationForm()
    context = {
        'form': form
        }
    # Render the make_reservation.html template with the form
    return render(request, 'make_reservation.html', context)

# Django view for searching reservations with user authentication. Handles both GET and POST requests. 


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

#  View that handles the reservations, so the user can see them


@login_required
def view_reservation(request):
    reservation = Reservation.objects.filter(user=request.user)
    context = {
        'reservation': reservation
        } 
    return render(request, 'view_reservation.html', context)

# View that handels edid/delete reservations


@login_required
def edit_or_delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    url = reverse('edit_or_delete_reservation', args=[reservation.id])
    
    if request.method == "POST":
        # Check if a 'delete' parameter is present in the POST data
        if 'delete' in request.POST:
            # Handle reservation deletion
            if reservation.delete():
                messages.success(request, 'Your reservation has been deleted.')
            return redirect('view_reservation')
        else:
            # Handle reservation editing
            form = ReservationForm(request.POST, instance=reservation)
            if form.is_valid():
                reservation = form.save()
                reservation.user = request.user
                reservation.save()
                messages.success(request, 'Your reservation has been updated.')
        return redirect('view_reservation')

    form = ReservationForm(instance=reservation)
    context = {
        'form': form
    }
    return render(request, 'edit_or_delete_reservation.html', context)
