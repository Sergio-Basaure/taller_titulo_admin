# Generated by Django 3.2.8 on 2021-12-05 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaServicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Descripcion')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('imagen', models.URLField(max_length=250)),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateField(auto_now=True, verbose_name='fecha de actualización')),
            ],
            options={
                'verbose_name': 'Categoria Servicio',
                'verbose_name_plural': 'Categorias Servicios',
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('descripcion', models.TextField(max_length=300, verbose_name='Descripción')),
                ('precio', models.IntegerField()),
                ('imagen', models.URLField(max_length=250)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateField(auto_now=True, verbose_name='fecha de actualización')),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.categoriaservicio')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
    ]
