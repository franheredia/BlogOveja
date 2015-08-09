# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0007_auto_20150809_0520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=50, verbose_name=b'autor')),
                ('comentario', models.TextField(max_length=500, verbose_name=b'comentario')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name=b'fecha')),
                ('post', models.ForeignKey(to='pagina.Entrada')),
            ],
        ),
    ]
