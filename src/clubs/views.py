"""Beside registering club view other views are related to ticket management
around specific flight, because Club model is used only by Flight model in this
app version then dispatching is done from flights.urls module.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from .forms import ClubForm, TicketForm
from .models import Club, Ticket
from manifest.models import Flight


@require_http_methods(["GET", "POST"])
def register_club(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        if Club.objects.all().count() >= 1:
            return redirect('home')
        else:
            form = ClubForm()
    args = {'form': form}
    return render(request, 'club.html', args)


@login_required
@require_http_methods(["GET", "POST"])
def plan_flight_view(request, pk):
    related_flight = Flight.objects.get(id=pk)
    initial_data = {'flights': related_flight}
    if request.user.has_perm('manifest.flight_add', 'clubs.ticket_add'):
        if request.method == 'POST':
            form_ticket = TicketForm(request.POST, prefix='form_ticket')
            if form_ticket.is_valid():
                form = form_ticket.save(commit=False)
                form.flight = related_flight
                form.save()
                return redirect('flights_list')
        else:
            if related_flight.seats_left > 0:
                form_ticket = TicketForm(prefix='form_ticket',
                                         initial=initial_data)
                args = {'related_flight': related_flight,
                        'ticket_add_form': form_ticket}
            else:
                return redirect('flights_list')
    else:
        return redirect('flights_list')
    return render(request, 'plan_flight.html', args)


@login_required
@require_http_methods(["POST"])
def unplan_flight_view(request, pk):
    # TODO: enclose in try except...
    if request.user.has_perm('manifest.flight_delete', 'clubs.ticket_delete')\
            and request.method == "POST":
        related_flight = get_object_or_404(Flight, id=pk)
        _reorder_flights_after(related_flight)
        related_flight.delete()
        return redirect('flights_list')
    else:
        return redirect('flights_list')


def _reorder_flights_after(given_flight: Flight):
    flights_at_date = Flight.objects.filter(date=given_flight.date).order_by('order_number')
    for flight in flights_at_date:
        if flight.order_number > given_flight.order_number:
            flight.order_number -= 1
            flight.save()


@login_required
@require_http_methods(["POST"])
def cancel_ticket_view(request, pk):
    if request.user.has_perm('clubs.ticket_delete') and request.method == "POST":
        related_ticket = get_object_or_404(Ticket, id=pk)
        related_ticket.delete()
        return redirect('flights_list')
    else:
        return redirect('flights_list')
