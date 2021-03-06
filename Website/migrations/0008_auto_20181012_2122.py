# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-12 15:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0007_auto_20181012_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundtransfer',
            name='date',
            field=models.DateField(default=datetime.date(2018, 10, 12)),
        ),
        migrations.AlterField(
            model_name='fundtransfer',
            name='ime',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=datetime.date(2018, 10, 12)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
