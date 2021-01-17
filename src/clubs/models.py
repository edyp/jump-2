from django.db import models
from django.contrib.auth.models import Group, Permission


def create_base_perm_group():
    group, created = Group.objects.get_or_create(name='Basic Member')
    existing_perms = Permission.objects.all()
    greater_perms_contents = {'log entry',
                              'deck arrangement',
                              'group',
                              'permission',
                              'content type',
                              'session'}
    group_perms = []
    for perm in existing_perms:
        if perm.content_type.__str__() not in greater_perms_contents and 'view' in perm.name:
            group_perms.append(perm)
    group.permissions.set(group_perms)


class Club(models.Model):
    name            = models.CharField(max_length=200)
    location        = models.CharField(max_length=200)
    aircrafts       = models.ManyToManyField('aircrafts.Aircraft')

    def __str__(self):
        return self.name

    def save(self):
        super(Club, self).save()

        create_base_perm_group()


class Ticket(models.Model):
    bought_by              = models.ForeignKey('users.User', on_delete=models.PROTECT, null=True)
    luggage                = models.ForeignKey('parachutes.Parachute', on_delete=models.PROTECT, null=True)
    flights                = models.ForeignKey('manifest.Flight', on_delete=models.PROTECT, null=True)
    DEFAULT_FLIGHT_HEIGHTS = [('4000', 4000), ('2000', 2000), ('1000', 1000)]
    exit_height            = models.CharField(max_length=5, choices=DEFAULT_FLIGHT_HEIGHTS)
    price                  = models.DecimalField(max_digits=20, decimal_places=2)
