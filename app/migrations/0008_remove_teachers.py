# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 05:05
from __future__ import unicode_literals

from django.db import migrations


def forwards(apps, schema_editor):
    Teilnehmer = apps.get_model('app', 'Teilnehmer')
    Teilnehmer.objects.filter(is_teacher=True).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20160430_0006'),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
