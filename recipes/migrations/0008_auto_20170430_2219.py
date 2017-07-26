# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 22:19
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20170430_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='url',
            field=models.CharField(max_length=500, unique=True, validators=[django.core.validators.URLValidator]),
        ),
    ]
