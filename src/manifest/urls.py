from django.urls import path

from .views import FlightsListView, add_flight_view
from clubs.views import plan_flight_view, unplan_flight_view, cancel_ticket_view

urlpatterns = [
    path('', FlightsListView.as_view(), name='flights_list'),
    path('/add', add_flight_view, name='add_flight'),
    path('/<int:pk>', plan_flight_view, name='plan_flight'),
    path('/<int:pk>/delete', unplan_flight_view, name='unplan_flight'),
    path('/<int:pk>/delete_ticket', cancel_ticket_view, name='cancel_ticket')
]