# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Human', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='content',
            field=ckeditor.fields.RichTextField(default=1, verbose_name=b'??'),
            preserve_default=False,
        ),
    ]
