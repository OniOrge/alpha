# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_volunteer_volunteer'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='volunteer',
            field=models.TextField(blank=True, default='', verbose_name='Voluntario'),
        ),
    ]
