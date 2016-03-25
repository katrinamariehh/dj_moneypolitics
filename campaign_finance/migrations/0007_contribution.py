# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign_finance', '0006_auto_20160324_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cycle', models.IntegerField()),
                ('contrib_id', models.CharField(max_length=12)),
                ('contrib', models.CharField(max_length=50)),
                ('recip_id', models.CharField(max_length=9)),
                ('org_name', models.CharField(max_length=50)),
                ('ult_org', models.CharField(max_length=50, blank=True)),
                ('real_code', models.CharField(max_length=5)),
                ('amount', models.IntegerField()),
                ('recip_code', models.CharField(max_length=2)),
                ('transaction_type', models.CharField(max_length=3)),
                ('cmte_id', models.CharField(max_length=9)),
                ('other_id', models.CharField(max_length=9)),
                ('occupation', models.CharField(max_length=50)),
                ('employer', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
