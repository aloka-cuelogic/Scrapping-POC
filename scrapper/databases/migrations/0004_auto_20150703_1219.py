# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0003_auto_20150703_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='posted_on',
            field=models.DateField(null=True, blank=True),
        ),
    ]
