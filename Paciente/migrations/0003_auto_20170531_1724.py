# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-31 22:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Paciente', '0002_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='paciente',
            new_name='propietario',
        ),
    ]
