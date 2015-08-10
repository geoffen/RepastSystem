# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0003_auto_20150810_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='createTime',
            field=models.DateField(default=datetime.date(2015, 8, 10)),
        ),
    ]
