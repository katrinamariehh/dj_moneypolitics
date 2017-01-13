# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign_finance', '0007_contribution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='cycle',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='committee',
            name='active',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='committee',
            name='cycle',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='individual',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='individual',
            name='cycle',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pac',
            name='cycle',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pactopac',
            name='cycle',
            field=models.IntegerField(),
        ),
    ]
