# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20170629_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='en_address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ENGLISH ADDRESS'),
        ),
    ]