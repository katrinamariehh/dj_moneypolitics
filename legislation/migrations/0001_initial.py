# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Legislator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=15)),
                ('first_name', models.CharField(max_length=15)),
                ('leg_type', models.CharField(max_length=5)),
                ('state', models.CharField(max_length=2)),
                ('district', models.IntegerField()),
                ('party', models.CharField(max_length=30)),
                ('bioguide_id', models.CharField(max_length=15)),
                ('thomas_id', models.CharField(max_length=15)),
                ('opensecrets_id', models.CharField(max_length=15)),
                ('govtrack_id', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
