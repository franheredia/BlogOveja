# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0003_entrada_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='published',
        ),
        migrations.AddField(
            model_name='entrada',
            name='publicado',
            field=models.BooleanField(default=True, verbose_name='Publicado'),
            preserve_default=True,
        ),
    ]
