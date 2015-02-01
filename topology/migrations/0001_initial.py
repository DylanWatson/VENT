# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=16)),
                ('ip', models.CharField(unique=True, max_length=15)),
                ('number_of_threats', models.IntegerField(default=0)),
                ('threat_level', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('attacker', models.CharField(unique=True, max_length=15)),
                ('date', models.DateTimeField()),
                ('reciever', models.ForeignKey(to='topology.Machine')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
