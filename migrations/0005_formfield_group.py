# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-20 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_remove_office_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfield',
            name='group',
            field=models.CharField(default=b'data', max_length=64, verbose_name='Group'),
        ),
    ]