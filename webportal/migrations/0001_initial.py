# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upvotes', models.IntegerField(default=0)),
                ('Ques', models.CharField(max_length=1024)),
                ('ans', models.CharField(max_length=128)),
                ('option1', models.CharField(max_length=128)),
                ('option2', models.CharField(max_length=128)),
                ('option3', models.CharField(max_length=128)),
                ('status', models.CharField(default=b'closed', max_length=128)),
                ('starting_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.IntegerField(default=0)),
                ('ranking', models.IntegerField(default=-1)),
                ('school_iD', models.CharField(unique=True, max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('pincode', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_picture', models.CharField(default=b'', max_length=128)),
                ('points', models.IntegerField(default=0)),
                ('ranking', models.IntegerField(default=-1)),
                ('student_iD', models.CharField(unique=True, max_length=128)),
                ('fb_iD', models.CharField(max_length=128, blank=True)),
                ('school_name', models.CharField(max_length=128)),
                ('gender', models.CharField(max_length=128, blank=True)),
                ('name', models.CharField(max_length=128)),
                ('mobile_no', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_picture', models.CharField(default=b'https://github.com/identicons/jasonlong.png', max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('mobile_no', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('teaher_id', models.CharField(unique=True, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
