# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-17 14:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Maps',
            new_name='Map',
        ),
    ]
