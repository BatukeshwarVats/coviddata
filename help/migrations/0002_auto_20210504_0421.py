# Generated by Django 2.2.19 on 2021-05-04 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='address',
        ),
        migrations.RemoveField(
            model_name='info',
            name='disc',
        ),
    ]
