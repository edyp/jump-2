from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
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
    aircrafts       = models.ManyToManyField('aircrafts.Aircraft', blank=True)

    def __str__(self):
        return self.name

    def save(self):
        super(Club, self).save()
        create_base_perm_group()


class Ticket(models.Model):
    bought_by              = models.ForeignKey('users.User',
                                               on_delete=models.PROTECT,
                                               null=True,
                                               blank=True)
    luggage                = models.ForeignKey('parachutes.Parachute',
                                               on_delete=models.PROTECT,
                                               null=True,
                                               blank=True)
    flight                = models.ForeignKey('manifest.Flight',
                                               on_delete=models.CASCADE,
                                               null=True,
                                               blank=True)
    DEFAULT_FLIGHT_HEIGHTS = [('4000', 4000), ('2000', 2000), ('1000', 1000)]
    exit_height            = models.CharField(max_length=5,
                                              choices=DEFAULT_FLIGHT_HEIGHTS,
                                              default='4000')
    price                  = models.DecimalField(max_digits=20,
                                                 decimal_places=2,
                                                 blank=True,
                                                 default=0.00)
    notes                  = models.TextField(max_length=1500,
                                              blank=True,
                                              default='')


@receiver(pre_save, sender=Ticket)
def calculate_price(sender, instance, *args, **kwargs):
    # TODO: from Club's price list take proper values.
    price_list = {
        'flight': {'4000': 200, '2000': 150, '1000': 100},
        'parachute': 20
    }
    try:
        if instance.price != 0.00:
            calculated_price = instance.price
        else:
            calculated_price = price_list['flight'][str(instance.exit_height)]
            if instance.luggage.is_borrowed():
                calculated_price += price_list['parachute']
    except KeyError:
        # There is no exit_height added
        calculated_price = 0.00
    finally:
        instance.price = calculated_price
