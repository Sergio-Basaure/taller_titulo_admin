# Generated by Django 3.2.8 on 2021-10-14 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Usuario')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Correo electrónico')),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombres del usuario')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos del usuario')),
                ('rut', models.CharField(max_length=10, unique=True, verbose_name='Rut del usuario')),
                ('contacto', models.IntegerField(verbose_name='Contacto del usuario')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
            },
        ),
    ]
