from django.contrib import admin

from .models import Flight


class FlightAdmin(admin.ModelAdmin):
    list_display = ['date', 'status', 'available_seats', 'pilots_names']

admin.site.register(Flight, FlightAdmin)
