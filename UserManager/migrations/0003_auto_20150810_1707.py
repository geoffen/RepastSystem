# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0002_auto_20150810_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userInfo',
        ),
        migrations.AddField(
            model_name='userinformation',
            name='createTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='userinformation',
            name='password',
            field=models.CharField(default='test', max_length=16),
        ),
        migrations.AddField(
            model_name='userinformation',
            name='username',
            field=models.CharField(default='test', max_length=16),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
