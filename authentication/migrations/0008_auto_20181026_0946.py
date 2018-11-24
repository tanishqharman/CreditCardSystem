# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-26 04:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20181023_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Website.Account'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Website.Account'),
        ),
    ]
