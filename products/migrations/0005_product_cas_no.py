# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20170628_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cas_no',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='CAS NO'),
        ),
    ]
