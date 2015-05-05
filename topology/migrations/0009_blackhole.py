# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topology', '0008_remove_machine_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blackhole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(unique=True, max_length=15)),
                ('blackholed', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
