# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 20:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('palpites', '0002_auto_20170818_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='palpite',
            old_name='author',
            new_name='autor',
        ),
    ]
