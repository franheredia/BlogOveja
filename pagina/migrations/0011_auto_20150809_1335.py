# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0010_auto_20150809_0546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='coment',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='user',
        ),
        migrations.AddField(
            model_name='comentario',
            name='contenido',
            field=models.TextField(default=5, max_length=500, verbose_name=b'Ahi lo anoto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comentario',
            name='nick',
            field=models.CharField(default='User', max_length=50, verbose_name=b'publicado por:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha'),
        ),
    ]
