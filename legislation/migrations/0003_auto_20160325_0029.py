# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legislation', '0002_auto_20160325_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legislator',
            name='district',
            field=models.CharField(max_length=3),
            preserve_default=True,
        ),
    ]
