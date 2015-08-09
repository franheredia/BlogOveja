# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0002_auto_20150803_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='imagen',
            field=models.FileField(default=b'null', upload_to=b'imagenesdepost', verbose_name='Imagen del Post'),
            preserve_default=True,
        ),
    ]
