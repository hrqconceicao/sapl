# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-27 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0056_popula_materiaemtramitacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='MateriaEmTramitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'materia_materiaemtramitacao',
                'managed': False,
            },
        ),
    ]
