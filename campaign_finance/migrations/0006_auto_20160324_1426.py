# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign_finance', '0005_auto_20160324_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='microfilm',
            field=models.CharField(max_length=20),
        ),
    ]
