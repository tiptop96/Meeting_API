# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-15 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20171015_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='when',
            name='minuteDuration',
            field=models.CharField(max_length=3),
        ),
    ]
