# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-19 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20170304_1718'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Runner',
        ),
        migrations.AlterField(
            model_name='route',
            name='path_url',
            field=models.URLField(max_length=1000),
        ),
    ]
