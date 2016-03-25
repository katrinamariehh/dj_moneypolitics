# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legislation', '0004_auto_20160325_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='legislator',
            name='lis_id',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
