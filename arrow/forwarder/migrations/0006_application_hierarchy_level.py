# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-19 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forwarder', '0005_auto_20171106_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='hierarchy_level',
            field=models.IntegerField(default=0),
        ),
    ]