# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brutfoce', '0005_auto_20170611_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dictionary',
            field=models.PositiveSmallIntegerField(choices=[(1, b'Wszystkie'), (2, b'Cyfry'), (3, b'Ma\xc5\x82e litery'), (4, b'Du\xc5\xbce litery'), (5, b'Wszystkie litery'), (6, b'Ma\xc5\x82e litery i cyfry'), (7, b'Du\xc5\xbce litery i cyfry')], default=2),
        ),
    ]