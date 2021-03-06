# Generated by Django 2.1.2 on 2018-11-13 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_preference',
            name='employee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employee_preference',
            name='region',
            field=models.CharField(choices=[('교내', 'School'), ('서울대입구역', 'SNUStation'), ('녹두', 'Nokdu'), ('낙성대', 'Nakdae'), ('기타', 'Extra')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employer_introduction',
            name='employer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
