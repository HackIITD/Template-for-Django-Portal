# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webportal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_picture',
            field=models.CharField(default=b'https://avatars2.githubusercontent.com/u/163800', max_length=128),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='profile_picture',
            field=models.CharField(default=b'https://avatars2.githubusercontent.com/u/163800', max_length=128),
        ),
    ]
