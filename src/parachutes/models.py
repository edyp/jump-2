from django.db import models


class Parachute(models.Model):
    name         = models.CharField(max_length=50)
    size         = models.DecimalField(max_digits=4, decimal_places=0)
    total_weight = models.DecimalField(max_digits=3, decimal_places=0)

    def __str__(self):
        return ' '.join([self.name, str(self.size)])