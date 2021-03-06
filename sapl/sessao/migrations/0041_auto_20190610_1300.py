# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-10 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sessao', '0040_auto_20190523_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiposessaoplenaria',
            name='tipo_numeracao',
            field=models.PositiveIntegerField(choices=[(1, 'Quinzenal'), (2, 'Mensal'), (10, 'Anual'), (11, 'Sessão Legislativa'), (
                12, 'Legislatura'), (99, 'Numeração Única')], default=11, verbose_name='Tipo de Numeração'),
        ),
        migrations.AlterField(
            model_name='tiposessaoplenaria',
            name='nome',
            field=models.CharField(
                max_length=30, verbose_name='Descrição do Tipo'),
        ),
    ]
