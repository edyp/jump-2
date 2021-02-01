from django.urls import path

from .views import FlightsListView, add_flight_view
from clubs.views import plan_flight_view

urlpatterns = [
    path('', FlightsListView.as_view(), name='flights_list'),
    path('/add', add_flight_view, name='add_flight'),
    path('/<int:pk>', plan_flight_view, name='plan_flight')
]