# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-31 22:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sdr', '0002_videoconferencia_sessao_plenaria'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Videoconferencia',
            new_name='SistemaDeliberacaoRemota',
        ),
    ]
