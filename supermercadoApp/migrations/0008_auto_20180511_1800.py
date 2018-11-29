# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-11 18:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermercadoApp', '0007_auto_20180511_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 18, 0, 58, 475254)),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 18, 0, 58, 476156)),
        ),
        migrations.AlterField(
            model_name='mensaje_cliente',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 18, 0, 58, 473429)),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='fecha_adquisicion',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 18, 0, 58, 474847)),
        ),
    ]
