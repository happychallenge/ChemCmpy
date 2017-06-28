# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_contact_qq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='cn_address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='CHINESE ADDRESS'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='cn_name',
            field=models.CharField(max_length=50, verbose_name='CHINESE NAME'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='en_address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ENGLISH ADDRESS'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='en_name',
            field=models.CharField(max_length=50, verbose_name='ENGLISH NAME'),
        ),
    ]
