# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-11 12:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supermercadoApp', '0004_auto_20180511_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='MensajeProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='mensaje',
        ),
        migrations.AlterField(
            model_name='carrito',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 14, 6, 21, 975797)),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 14, 6, 21, 975797)),
        ),
        migrations.AlterField(
            model_name='mensaje_cliente',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 14, 6, 21, 975797)),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='fecha_adquisicion',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 11, 14, 6, 21, 975797)),
        ),
        migrations.AddField(
            model_name='mensajeproducto',
            name='mensaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermercadoApp.Mensaje_Cliente'),
        ),
        migrations.AddField(
            model_name='mensajeproducto',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='supermercadoApp.Producto'),
        ),
    ]
