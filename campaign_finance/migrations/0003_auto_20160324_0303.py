# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign_finance', '0002_auto_20160324_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committee',
            name='source',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
