# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-12 15:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0009_auto_20181012_2123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fundtransfer',
            old_name='ime',
            new_name='time',
        ),
    ]