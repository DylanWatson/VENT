# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topology', '0005_machine_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='slug',
        ),
    ]
