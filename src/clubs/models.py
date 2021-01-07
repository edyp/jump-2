from django.db import models


class Club(models.Model):
    name            = models.CharField(max_length=200)
    location        = models.CharField(max_length=200)
    aircrafts       = models.ManyToManyField('aircrafts.Aircraft')

    def __str__(self):
        return self.name


class Ticket(models.Model):
    bought_by              = models.ForeignKey('users.User', on_delete=models.PROTECT, null=True)
    luggage                = models.ForeignKey('parachutes.Parachute', on_delete=models.PROTECT, null=True)
    flights                = models.ForeignKey('manifest.Flight', on_delete=models.PROTECT, null=True)
    DEFAULT_FLIGHT_HEIGHTS = [('4000', 4000), ('2000', 2000), ('1000', 1000)]
    exit_height            = models.CharField(max_length=5, choices=DEFAULT_FLIGHT_HEIGHTS)
    price                  = models.DecimalField(max_digits=20, decimal_places=2)
