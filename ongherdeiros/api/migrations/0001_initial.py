# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_text', models.CharField(max_length=200, verbose_name='Titulo')),
                ('date_date', models.DateTimeField(verbose_name='Data do Evento')),
                ('local_text', models.CharField(max_length=200, verbose_name='Local')),
                ('description_text', models.CharField(max_length=500, verbose_name='Descricao')),
                ('image_src_text', models.CharField(max_length=100, verbose_name='Caminho da imagem')),
            ],
        ),
    ]
