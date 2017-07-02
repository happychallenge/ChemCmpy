# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 02:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20170630_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='gprelation',
            field=models.CharField(choices=[('CURRENT PROVIDER', 'CURRENT PROVIDER'), ('OLD PROVIDER', 'OLD PROVIDER'), ('NO RELATION', 'NO RELATION')], default='CURRENT PROVIDER', max_length=20),
        ),
        migrations.AlterField(
            model_name='provider',
            name='companytype',
            field=models.CharField(choices=[('T', 'TRADING'), ('M', 'MANUFACTURER'), ('X', 'MIXING')], default='M', max_length=20),
        ),
    ]
