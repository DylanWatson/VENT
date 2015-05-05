# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topology', '0003_auto_20150222_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threat',
            name='attacker',
            field=models.CharField(max_length=15),
        ),
    ]
