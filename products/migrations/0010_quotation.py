# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 04:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20170628_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('paytype', models.CharField(choices=[('R', 'RMB'), ('$', 'DOLLAR')], default='R', max_length=1)),
                ('quote_date', models.DateTimeField(auto_now_add=True)),
                ('effective_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('V', 'VALID'), ('I', 'IN-VALID')], default='V', max_length=1)),
                ('comments', models.TextField(blank=True, null=True)),
                ('companyproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.CompanyProduct')),
            ],
        ),
    ]
