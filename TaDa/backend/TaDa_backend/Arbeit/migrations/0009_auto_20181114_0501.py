# Generated by Django 2.1.2 on 2018-11-14 05:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arbeit', '0008_auto_20181114_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbeit',
            name='edit_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 14, 5, 1, 10, 907064), verbose_name='date edited'),
        ),
        migrations.AlterField(
            model_name='arbeit',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 14, 5, 1, 10, 907064), verbose_name='date published'),
        ),
    ]
