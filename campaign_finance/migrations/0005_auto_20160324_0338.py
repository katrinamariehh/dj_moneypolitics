# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign_finance', '0004_auto_20160324_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='date',
            field=models.DateField(blank=True),
            preserve_default=True,
        ),
    ]
