# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('menu', '0002_auto_20170405_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_name',
            field=models.CharField(max_length=128),
        ),
    ]
