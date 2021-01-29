from django.db import models


class Parachute(models.Model):
    name         = models.CharField(max_length=50)
    size         = models.DecimalField(max_digits=4, decimal_places=0)
    total_weight = models.DecimalField(max_digits=3, decimal_places=0)
    rental       = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} {str(self.size)}'

    def is_borrowed(self):
        return self.rental
