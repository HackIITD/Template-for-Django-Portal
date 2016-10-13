# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webportal', '0002_auto_20161013_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='ranking',
            field=models.IntegerField(default=-1),
        ),
    ]
