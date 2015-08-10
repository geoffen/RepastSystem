# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0006_auto_20150810_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='createTime',
            field=models.DateField(default=datetime.date(2015, 8, 10)),
        ),
    ]
