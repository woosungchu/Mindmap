# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-02 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0009_auto_20170302_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='title',
            field=models.CharField(default='Untitled', max_length=100),
        ),
        migrations.AlterField(
            model_name='node',
            name='type',
            field=models.CharField(default='Node', max_length=50),
        ),
    ]
