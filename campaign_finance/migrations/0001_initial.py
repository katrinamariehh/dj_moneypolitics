# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cycle', models.IntegerField(max_length=4)),
                ('fec_cand_id', models.CharField(max_length=9)),
                ('cid', models.CharField(max_length=9)),
                ('first_last_p', models.CharField(max_length=50)),
                ('party', models.CharField(max_length=1)),
                ('dis_id_run_for', models.CharField(max_length=4)),
                ('dis_id_curr', models.CharField(max_length=4)),
                ('curr_cand', models.CharField(max_length=1)),
                ('cycle_cand', models.CharField(max_length=1)),
                ('crpico', models.CharField(max_length=1)),
                ('recip_code', models.CharField(max_length=2)),
                ('no_pacs', models.CharField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cycle', models.IntegerField(max_length=4)),
                ('cmte_id', models.CharField(max_length=9)),
                ('pac_short', models.CharField(max_length=50)),
                ('affiliate', models.CharField(max_length=50)),
                ('ultorg', models.CharField(max_length=50)),
                ('recip_id', models.CharField(max_length=9)),
                ('recip_code', models.CharField(max_length=2)),
                ('fec_cand_id', models.CharField(max_length=9)),
                ('party', models.CharField(max_length=1)),
                ('prim_code', models.CharField(max_length=5)),
                ('source', models.CharField(max_length=5)),
                ('sensitive', models.CharField(max_length=1)),
                ('foreign', models.CharField(max_length=1)),
                ('active', models.IntegerField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cycle', models.IntegerField(max_length=4)),
                ('fec_trans_id', models.CharField(max_length=19)),
                ('contrib_id', models.CharField(max_length=12)),
                ('contrib', models.CharField(max_length=50)),
                ('recip_id', models.CharField(max_length=9)),
                ('org_name', models.CharField(max_length=50)),
                ('ultorg', models.CharField(max_length=50, blank=True)),
                ('real_code', models.CharField(max_length=5)),
                ('date', models.DateField()),
                ('amount', models.IntegerField(max_length=30)),
                ('zip_code', models.CharField(max_length=5)),
                ('recip_code', models.CharField(max_length=2)),
                ('transaction_type', models.CharField(max_length=3)),
                ('cmte_id', models.CharField(max_length=9)),
                ('other_id', models.CharField(max_length=9)),
                ('gender', models.CharField(max_length=1)),
                ('microfilm', models.CharField(max_length=11)),
                ('occupation', models.CharField(max_length=50)),
                ('employer', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pac',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cycle', models.IntegerField(max_length=4)),
                ('fec_rec_no', models.CharField(max_length=19)),
                ('pac_id', models.CharField(max_length=9)),
                ('cid', models.CharField(max_length=9)),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('real_code', models.CharField(max_length=5)),
                ('transaction_type', models.CharField(max_length=3)),
                ('di', models.CharField(max_length=1)),
                ('fec_cand_id', models.CharField(max_length=9)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PacToPac',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cycle', models.IntegerField(max_length=4)),
                ('fec_rec_no', models.CharField(max_length=19)),
                ('filer_id', models.CharField(max_length=8)),
                ('donor_cmte', models.CharField(max_length=50)),
                ('contrib_lend_trans', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.CharField(max_length=5)),
                ('fec_occ_emp', models.CharField(max_length=38)),
                ('prim_code', models.CharField(max_length=5)),
                ('date', models.DateField()),
                ('amount', models.FloatField()),
                ('recip_id', models.CharField(max_length=9)),
                ('party', models.CharField(max_length=1)),
                ('other_id', models.CharField(max_length=9)),
                ('recip_code', models.CharField(max_length=2)),
                ('recip_prim_code', models.CharField(max_length=5)),
                ('amend', models.CharField(max_length=1)),
                ('report', models.CharField(max_length=3)),
                ('pg', models.CharField(max_length=2)),
                ('microfilm', models.CharField(max_length=11)),
                ('transaction_type', models.CharField(max_length=3)),
                ('real_code', models.CharField(max_length=5)),
                ('source', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
