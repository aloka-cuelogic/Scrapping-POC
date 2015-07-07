# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('adverties_id', models.CharField(max_length=150, unique=True, null=True, blank=True)),
                ('title', models.CharField(max_length=100, null=True, blank=True)),
                ('property_url', models.URLField(null=True, blank=True)),
                ('location', models.CharField(blank=True, max_length=250, null=True, choices=[(b'1', b'RK'), (b'2', b'1 BHK'), (b'3', b'2 BHK'), (b'4', b'3 BHK'), (b'5', b'4 BHK')])),
                ('description', models.TextField(null=True, blank=True)),
                ('monthly_rent', models.IntegerField(null=True, blank=True)),
                ('property_type', models.CharField(max_length=50, null=True, blank=True)),
                ('posted_on', models.DateField(null=True, blank=True)),
            ],
        ),
    ]
