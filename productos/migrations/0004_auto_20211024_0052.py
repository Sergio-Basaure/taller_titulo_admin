# Generated by Django 3.2.8 on 2021-10-24 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20211023_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriaproducto',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True, verbose_name='fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='categoriaproducto',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
    ]
