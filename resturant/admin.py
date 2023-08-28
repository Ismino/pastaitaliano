from django.contrib import admin
from .models import Table, Reservation

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('seats', 'min_people', 'max_people',)
    list_filter = ('seats', 'min_people', 'max_people',)
    search_fields = ('customer__username', 'customer')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('table', 'customer', 'reservation_datetime', 'status',)
    list_filter = ('table', 'customer', 'reservation_datetime','status',)
    search_fields = ('customer__username', 'customer')
    actions = ['cancel_reservations', 'mark_completed']

    def cancel_reservations(self, request, queryset):
        queryset.update(status=2)  
    cancel_reservations.short_description = "Cancel selected reservations"

    def mark_completed(self, request, queryset):
        queryset.update(status=3)  
    mark_completed.short_description = "Mark selected reservations as Completed"


