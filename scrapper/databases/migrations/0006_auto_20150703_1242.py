# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0005_auto_20150703_1237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='type',
            new_name='property_type',
        ),
    ]
