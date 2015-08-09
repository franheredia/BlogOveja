# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrada',
            name='imagen',
        ),
        migrations.AddField(
            model_name='entrada',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Publicado?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entrada',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Post'),
            preserve_default=True,
        ),
    ]
