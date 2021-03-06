# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 09:38
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20160526_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teilnehmer',
            name='hobbies',
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=255),
                blank=True,
                default=list,
                help_text='Durch ein Komma getrennt',
                size=None,
                verbose_name='hobbies'),
        ),
    ]
