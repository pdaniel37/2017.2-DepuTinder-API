# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-07 02:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('propositions', '0003_propositions_questionnaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propositions',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propositionID', to='questionnaire.Questionnaire'),
        ),
    ]
