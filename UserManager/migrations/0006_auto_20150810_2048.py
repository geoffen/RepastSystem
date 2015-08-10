# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0005_auto_20150810_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='createTime',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
