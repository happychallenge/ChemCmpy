# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20170702_1128'),
    ]

    operations = [

        migrations.AddField(
            model_name='vendor',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
