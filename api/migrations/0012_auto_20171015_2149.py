# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-15 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20171015_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='when',
            name='duration',
            field=models.CharField(default='', help_text='In minutes', max_length=3),
        ),
    ]
