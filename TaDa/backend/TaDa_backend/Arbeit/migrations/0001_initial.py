# Generated by Django 2.1.2 on 2018-11-13 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Arbeit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('content', models.TextField(null=True)),
                ('pay', models.IntegerField(default=0)),
                ('manager_name', models.CharField(max_length=50, null=True)),
                ('manager_phone', models.CharField(max_length=50, null=True)),
                ('register_date', models.DateTimeField(verbose_name='date published')),
                ('edit_date', models.DateTimeField(verbose_name='date edited')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
