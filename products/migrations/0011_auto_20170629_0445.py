# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 04:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_quotation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='effective_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
