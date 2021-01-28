from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.decorators.http import require_http_methods
from .models import Flight
from .forms import FlightAddForm


class FlightsListView(ListView):

    model = Flight
    paginate_by = 2
    template_name = 'flight_list.html'

    def get_context_data(self, **kwargs):
        sort_val = self.request.GET.get('sort', 'date')
        filter_val = self.request.GET.get('filter', '')
        all_flights_qs = super().get_queryset().order_by(sort_val)
        if filter_val:
            all_flights_qs = all_flights_qs.filter(date=filter_val)
        context = super().get_context_data(object_list=all_flights_qs)
        context['sort'] = sort_val
        context['filter'] = filter_val
        return context


@require_http_methods(["GET", "POST"])
def add_flight_view(request):
    if request.method == 'POST':
        form = FlightAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flights-list')
    else:
        form = FlightAddForm()
        args = {'flight_add_form': form}
    return render(request, 'add_flight.html', args)

