# Generated by Django 2.2.16 on 2021-01-07 21:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manifest', '0011_auto_20210106_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='date',
            field=models.DateField(default=datetime.date(2021, 1, 7)),
        ),
    ]
