# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0006_auto_20150703_1242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='description',
            new_name='pro_description',
        ),
    ]
