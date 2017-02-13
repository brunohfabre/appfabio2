# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 16:44
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170209_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Um nome curto que ser\xe1 usado para identific\xe1-lo de forma \xfanica na plataforma', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'Informe um nome de usu\xe1rio v\xe1lido. Este valor deve conter apenas letras, n\xfameros e os caracteres: @/./+/-/_ .', 'invalid')], verbose_name='Nome de Usu\xe1rio'),
        ),
    ]
