# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-15 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20171015_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='adress',
            field=models.CharField(help_text='Street, City, Country (Please activate javascript for autofill)', max_length=96),
        ),
        migrations.AlterField(
            model_name='when',
            name='day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thusday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=10),
        ),
    ]
