# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-03 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=96, unique=True)),
                ('country', models.CharField(blank=True, max_length=96, unique=True)),
                ('city', models.CharField(blank=True, max_length=96, unique=True)),
                ('street', models.CharField(blank=True, max_length=96, unique=True)),
                ('start_time', models.TimeField(blank=True, max_length=96, unique=True)),
                ('end_time', models.TimeField(blank=True, max_length=96, unique=True)),
                ('monday', models.BooleanField(default=False)),
                ('tuesday', models.BooleanField(default=False)),
                ('wednesday', models.BooleanField(default=False)),
                ('thursday', models.BooleanField(default=False)),
                ('friday', models.BooleanField(default=False)),
                ('saturday', models.BooleanField(default=False)),
                ('sunday', models.BooleanField(default=False)),
            ],
        ),
    ]
