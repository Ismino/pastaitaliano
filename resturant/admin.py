from django.contrib import admin
from .models import Table, Reservation

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('seats', 'min_people', 'max_people',)
    list_filter = ('seats', 'min_people', 'max_people',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('table', 'customer', 'reservation_datetime', 'status',)
    list_filter = ('table', 'customer', 'reservation_datetime','status',)
    search_fields = ('customer__username',)