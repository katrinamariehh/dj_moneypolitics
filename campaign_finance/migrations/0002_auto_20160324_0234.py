# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign_finance', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='dis_id_curr',
            new_name='dist_id_curr',
        ),
        migrations.RenameField(
            model_name='candidate',
            old_name='dis_id_run_for',
            new_name='dist_id_run_for',
        ),
    ]
