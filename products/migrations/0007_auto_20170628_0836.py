# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20170628_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='usage',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='용도'),
        ),
    ]
