# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0007_auto_20150703_1310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='pro_description',
            new_name='description',
        ),
    ]
