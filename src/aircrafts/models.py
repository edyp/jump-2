from django.db import models


class Aircraft(models.Model):
    name                      = models.CharField(max_length=50)
    permitted_starting_weight = models.DecimalField(max_digits=5, decimal_places=0)
    seats_configuration       = models.ManyToManyField('DeckArrangement')

    def __str__(self):
        return self.name


class DeckArrangement(models.Model):
    max_pilot_seats = models.IntegerField('maximal number of pilots in arrangement')
    max_passenger_seats = models.IntegerField('maximal number of passengers in arrangement')

    def __str__(self):
        return '/'.join([str(self.max_pilot_seats), str(self.max_passenger_seats)])