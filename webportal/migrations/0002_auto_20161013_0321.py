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
            name='points',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='ranking',
            field=models.IntegerField(),
        ),
    ]
