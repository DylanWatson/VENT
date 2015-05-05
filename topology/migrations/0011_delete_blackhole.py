# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topology', '0010_blackhole_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blackhole',
        ),
    ]
