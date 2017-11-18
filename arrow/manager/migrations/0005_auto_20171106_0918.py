# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-06 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20171106_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationtype',
            name='name',
            field=models.CharField(choices=[('SSLC', 'SSLC'), ('+2', '+2'), ('EMB', 'Embassy Attestation'), ('BNK1', 'Bank Loan - 1 Year'), ('BNK4', 'Bank Loan - 4 Years'), ('CHAR', 'Character Certificate'), ('NRSD', 'Non Receipt of Stipend'), ('NRLP', 'Non Receipt of Laptop'), ('NRSP', 'Non Receipt of Scholarship'), ('OTH', 'Other')], max_length=4, unique=True),
        ),
    ]
