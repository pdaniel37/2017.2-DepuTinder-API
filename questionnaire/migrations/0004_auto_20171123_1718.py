# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0003_auto_20171031_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionnaire',
            name='questionnaireID',
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]