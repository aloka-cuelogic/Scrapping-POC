# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0004_auto_20150703_1219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='property_unique_id',
            new_name='adverties_id',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='rent',
            new_name='monthly_rent',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='bedrooms',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='property',
            name='location',
            field=models.CharField(blank=True, max_length=250, null=True, choices=[(b'1', b'RK'), (b'2', b'1 BHK'), (b'3', b'2 BHK'), (b'4', b'3 BHK'), (b'5', b'4 BHK')]),
        ),
    ]
