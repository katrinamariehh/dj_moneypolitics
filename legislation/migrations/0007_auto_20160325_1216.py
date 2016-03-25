# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legislation', '0006_bill_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='legislator_id_type',
            field=models.CharField(max_length=15),
            preserve_default=True,
        ),
    ]
