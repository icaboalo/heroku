# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-27 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='slug',
            field=models.SlugField(blank=True, max_length=52, unique=True),
        ),
    ]