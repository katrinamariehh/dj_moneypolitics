# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign_finance', '0003_auto_20160324_0303'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual',
            name='city',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='individual',
            name='state',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='individual',
            name='street',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
