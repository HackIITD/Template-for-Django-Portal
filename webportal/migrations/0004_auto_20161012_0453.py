# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webportal', '0003_auto_20161012_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_picture',
            field=models.CharField(default=b'https://help.github.com/assets/images/help/profile/identicon.png', max_length=128),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='profile_picture',
            field=models.CharField(default=b'https://help.github.com/assets/images/help/profile/identicon.png', max_length=128),
        ),
    ]
