# Generated by Django 3.2.8 on 2021-10-18 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_alter_cliente_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='last_login',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='last login'),
        ),
    ]
