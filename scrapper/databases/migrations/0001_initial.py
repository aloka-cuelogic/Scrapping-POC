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
                ('property_unique_id', models.CharField(max_length=150, unique=True, null=True, blank=True)),
                ('title', models.CharField(max_length=100, null=True, blank=True)),
                ('property_url', models.URLField(null=True, blank=True)),
                ('location', models.CharField(max_length=50, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('rent', models.IntegerField(null=True, blank=True)),
                ('bedrooms', models.CharField(max_length=50, null=True, blank=True)),
                ('posted_on', models.DateField(null=True, blank=True)),
            ],
        ),
    ]
