# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 16:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Brutfoce', '0004_auto_20170611_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='discription',
            new_name='description',
        ),
    ]