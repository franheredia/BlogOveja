# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Titulo de la Categoria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='T\xedtulo')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('resumen', models.CharField(max_length=512, verbose_name='Resumen')),
                ('contenido', models.TextField(verbose_name='Contenido')),
                ('imagen', models.FileField(default=b'null', upload_to=b'imagendepost', verbose_name='ImagenPost')),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(to='pagina.Categoria')),
            ],
            options={
                'ordering': ['-fecha'],
            },
            bases=(models.Model,),
        ),
    ]
