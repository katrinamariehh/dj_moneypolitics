# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legislation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legislator',
            name='district',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
    ]
