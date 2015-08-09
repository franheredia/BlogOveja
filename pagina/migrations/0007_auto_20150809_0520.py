# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0006_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='post',
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]
