# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propositions', '0004_auto_20171007_0228'),
    ]

    operations = [
        migrations.AddField(
            model_name='propositions',
            name='propositionLink',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]