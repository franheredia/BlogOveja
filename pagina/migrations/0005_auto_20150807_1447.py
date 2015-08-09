# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0004_auto_20150807_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entrada',
            options={'ordering': ['-fecha'], 'verbose_name': 'Entrada', 'verbose_name_plural': 'Entradas'},
        ),
    ]
