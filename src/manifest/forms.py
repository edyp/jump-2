from django import forms
from .models import Flight


class FlightAddForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ('date', 'club', 'aircraft', 'available_seats', 'pilots',)
