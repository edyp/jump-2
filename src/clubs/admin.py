from django.contrib import admin

from .models import Club, Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ['bought_by', 'luggage', 'flights', 'exit_height', 'price']


admin.site.register(Club)
admin.site.register(Ticket, TicketAdmin)
