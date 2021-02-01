from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from .forms import ClubForm, TicketForm
from .models import Club
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
                form.flights = related_flight
                form.save()
                return redirect('flights_list')
        else:
            form_ticket = TicketForm(prefix='form_ticket',
                                     initial=initial_data)
            args = {'related_flight': related_flight,
                    'ticket_add_form': form_ticket}
    else:
        return redirect('flights_list')
    return render(request, 'plan_flight.html', args)
