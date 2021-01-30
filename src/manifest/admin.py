from django.contrib import admin

from .models import Flight


class FlightAdmin(admin.ModelAdmin):
    list_display = ['order_number',
                    'date',
                    'status',
                    'available_seats',
                    'pilots_names']


admin.site.register(Flight, FlightAdmin)
