# Generated by Django 2.2.16 on 2021-01-04 07:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('manifest', '0006_auto_20210104_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='arrival_time',
            field=models.DateTimeField(default=datetime.date(2021, 1, 4)),
        ),
        migrations.AlterField(
            model_name='flight',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 1, 4, 7, 41, 39, 255344, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_time',
            field=models.DateTimeField(default=datetime.date(2021, 1, 4)),
        ),
    ]
