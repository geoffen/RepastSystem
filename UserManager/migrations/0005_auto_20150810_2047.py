# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('UserManager', '0004_auto_20150810_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('countryName', models.CharField(default='none', max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='createTime',
            field=models.DateField(default=datetime.datetime(2015, 8, 10, 12, 47, 17, 504000, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='userinformation',
            name='country',
            field=models.ForeignKey(default=datetime.datetime(2015, 8, 10, 12, 47, 48, 155000, tzinfo=utc), to='UserManager.Country'),
            preserve_default=False,
        ),
    ]
