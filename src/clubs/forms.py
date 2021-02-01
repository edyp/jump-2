from django import forms

from .models import Club, Ticket


class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ('name', 'location', 'aircrafts',)


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ['flights']
