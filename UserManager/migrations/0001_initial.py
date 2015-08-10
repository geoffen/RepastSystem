# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('countryName', models.CharField(default='none', max_length=30)),
                ('capital', models.CharField(default='none', max_length=30)),
                ('population', models.IntegerField(default=12)),
                ('countryCode', models.CharField(default='+86', max_length=5)),
            ],
            options={
                'ordering': ['countryName'],
            },
        ),
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default='test', max_length=16)),
                ('password', models.CharField(default='test', max_length=16)),
                ('createTime', models.DateField(default=django.utils.timezone.now, null=True, blank=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.ForeignKey(to='UserManager.Country')),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
    ]
