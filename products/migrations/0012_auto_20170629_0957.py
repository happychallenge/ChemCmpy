# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 09:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0011_auto_20170629_0445'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CompanyProduct',
            new_name='ProviderProduct',
        ),
        migrations.AlterModelOptions(
            name='quotation',
            options={'ordering': ['-quote_date']},
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='provider',
            name='status',
            field=models.CharField(choices=[('A', 'ACTIVE'), ('I', 'INACTIVE'), ('B', 'BANKRUPT')], default='A', max_length=1),
        ),
    ]
