# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-11 07:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supermercadoApp', '0002_auto_20180511_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='detalle',
        ),
        migrations.AddField(
            model_name='detallefactura',
            name='factura',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='supermercadoApp.Factura'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carrito',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 9, 58, 11, 833225)),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 9, 58, 11, 833225)),
        ),
        migrations.AlterField(
            model_name='mensaje_cliente',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 9, 58, 11, 833225)),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='fecha_adquisicion',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 9, 58, 11, 833225)),
        ),
    ]
