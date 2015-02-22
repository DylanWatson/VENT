# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topology', '0002_auto_20150222_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='threat_level',
        ),
        migrations.AlterField(
            model_name='threat',
            name='reciever',
            field=models.ForeignKey(to='topology.Machine', to_field=b'ip'),
        ),
    ]
