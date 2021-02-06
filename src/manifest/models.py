from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone


class Flight(models.Model):
    order_number    = models.IntegerField(null=True, blank=True)
    date            = models.DateField(max_length=10, default=timezone.now().date())
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

    @property
    def pilots_names(self):
        names = []
        for pilot in self.pilots.all():
            names.append(pilot.profile.__str__())
        return ', '.join(names)

    @property
    def seats_left(self):
        sold_tickets = self.ticket_set.all().count()
        return self.available_seats - sold_tickets

    def __str__(self):
        return f'{str(self.date)}/{self.order_number}'


@receiver(pre_save, sender=Flight)
def assign_flight_number(sender, instance, *args, **kwargs):
    '''Every flight should have order number for simpler recognition.
    Count and assign order number to flight before saving.'''
    if instance.order_number is None:
        preceding_flights_number = Flight.objects.filter(date=instance.date).count()
        instance.order_number = preceding_flights_number + 1
