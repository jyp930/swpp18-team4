# Generated by Django 2.1.2 on 2018-11-13 19:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Arbeit', '0006_auto_20181114_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbeit',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 13, 19, 52, 39, 50104, tzinfo=utc), verbose_name='date published'),
        ),
    ]
