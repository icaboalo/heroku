# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-25 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0009_auto_20160225_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='kid',
            name='full_name',
            field=models.CharField(default=1, max_length=150, unique=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kid',
            name='last_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kid',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]