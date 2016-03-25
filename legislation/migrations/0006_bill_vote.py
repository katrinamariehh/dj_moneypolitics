# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legislation', '0005_legislator_lis_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('congress', models.IntegerField()),
                ('bill_type', models.CharField(max_length=5)),
                ('title', models.CharField(max_length=50, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bill_id', models.CharField(max_length=10)),
                ('vote_id', models.CharField(max_length=30)),
                ('legislator_id', models.CharField(max_length=15)),
                ('legislator_id_type', models.CharField(max_length=10)),
                ('vote_value', models.CharField(max_length=15)),
                ('vote_type', models.CharField(max_length=15)),
                ('bill_object', models.ForeignKey(to='legislation.Bill')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
