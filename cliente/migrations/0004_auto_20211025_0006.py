# Generated by Django 3.2.8 on 2021-10-25 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_alter_cliente_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True, verbose_name='fecha de actualización'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
    ]