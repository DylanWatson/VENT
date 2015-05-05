# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('topology', '0009_blackhole'),
    ]

    operations = [
        migrations.AddField(
            model_name='blackhole',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
            preserve_default=True,
        ),
    ]
