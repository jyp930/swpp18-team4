# Generated by Django 2.1.2 on 2018-11-13 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arbeit', '0002_auto_20181113_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='arbeit',
            name='arbeit',
            field=models.CharField(choices=[('Mentoring', 'Mentoring'), ('Tutoring', 'Tutoring'), ('Cafe', 'Cafe'), ('IT', 'IT'), ('Design', 'Design'), ('Extra', 'Extra')], default='Extra', max_length=2),
        ),
        migrations.AddField(
            model_name='arbeit',
            name='region',
            field=models.CharField(choices=[('School', 'School'), ('SNUStation', 'SNUStation'), ('Nokdu', 'Nokdu'), ('Nakdae', 'Nakdae'), ('Extra', 'Extra')], default='Extra', max_length=2),
        ),
    ]
