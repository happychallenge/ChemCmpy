# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 11:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20170702_0642'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['en_name']},
        ),
        migrations.AlterModelOptions(
            name='quotation',
            options={'ordering': ['-status', '-quote_date']},
        ),
        migrations.AlterModelOptions(
            name='vendor',
            options={'ordering': ['gprelation', 'cn_name']},
        ),
        migrations.AlterField(
            model_name='contact',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Vendor'),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='quote_date',
            field=models.DateTimeField(),
        ),
    ]
