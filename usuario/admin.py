from django.contrib import admin
from clases_abstracta.admin import AbstractaAdmin
from .models import *
from import_export import resources

class Usuarioresource(resources.ModelResource):
    class Meta:
        model = Usuario

class UsuarioAdmin(AbstractaAdmin):
    search_fields = ('username', 'email', 'nombres', 'apellidos', 'rut',)
    list_display = ('nombres', 'apellidos', 'rut', 'contacto', 'is_active', 'is_staff', 'is_superuser')
    # exclude = ('password',)
    readonly_fields = ('last_login','groups', 'username', 'user_permissions')
    resource_class = Usuarioresource

admin.site.register(Usuario, UsuarioAdmin)
