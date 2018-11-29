# Generated by Django 2.0.5 on 2018-05-17 20:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermercadoApp', '0020_auto_20180517_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='cli_descuento',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 17, 20, 4, 53, 593877)),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 17, 20, 4, 53, 594933)),
        ),
        migrations.AlterField(
            model_name='mensaje_cliente',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 17, 20, 4, 53, 591495)),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='fecha_adquisicion',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 17, 20, 4, 53, 593526)),
        ),
    ]