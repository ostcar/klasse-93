# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 22:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='teilnehmer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Teilnehmer'),
            preserve_default=False,
        ),
    ]