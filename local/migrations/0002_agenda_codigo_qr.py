# Generated by Django 3.2.8 on 2021-12-13 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='codigo_qr',
            field=models.ImageField(blank=True, null=True, upload_to='qr'),
        ),
    ]