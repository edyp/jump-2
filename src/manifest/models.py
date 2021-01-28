from django.db import models
from django.utils import timezone


class Flight(models.Model):
    date            = models.DateField(default=timezone.now().date())
    departure_time  = models.DateTimeField(default=None, null=True, blank=True)
    arrival_time    = models.DateTimeField(default=None, null=True, blank=True)
    FLIGHT_STATUSES = [
        ('NEW', 'New'),
        ('B_F', 'Ready To Fly'),
        ('ONG', 'In Air'),
        ('LND', 'Landed')
    ]
    status          = models.CharField(max_length=3,
                                       choices=FLIGHT_STATUSES,
                                       default='NEW')
    aircraft        = models.ForeignKey('aircrafts.Aircraft',
                                        on_delete=models.PROTECT)
    club            = models.ForeignKey('clubs.Club',
                                        on_delete=models.PROTECT)
    available_seats = models.IntegerField(null=True)
    pilots          = models.ManyToManyField('users.User')
