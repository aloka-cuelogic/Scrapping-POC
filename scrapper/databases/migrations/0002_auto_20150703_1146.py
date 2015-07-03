# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='location',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
    ]
