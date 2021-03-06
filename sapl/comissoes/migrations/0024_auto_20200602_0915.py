# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-02 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comissoes', '0023_auto_20191211_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composicao',
            name='comissao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comissoes.Comissao', verbose_name='Comissão'),
        ),
        migrations.AlterField(
            model_name='participacao',
            name='composicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participacao_set', to='comissoes.Composicao', verbose_name='Composição'),
        ),
    ]
