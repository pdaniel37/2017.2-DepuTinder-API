# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-20 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='ansewrType',
        ),
        migrations.AddField(
            model_name='answers',
            name='answerType',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
