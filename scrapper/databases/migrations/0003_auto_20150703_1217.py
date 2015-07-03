# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0002_auto_20150703_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='posted_on',
            field=models.DateTimeField(max_length=250, null=True, blank=True),
        ),
    ]
