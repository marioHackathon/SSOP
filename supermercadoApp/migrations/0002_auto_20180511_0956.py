# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-11 07:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermercadoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallefactura',
            name='prod_cantidad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='prod_total',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carrito',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 9, 56, 30, 477737)),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 9, 56, 30, 477737)),
        ),
        migrations.AlterField(
            model_name='mensaje_cliente',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 9, 56, 30, 477737)),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='fecha_adquisicion',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 9, 56, 30, 477737)),
        ),
    ]
