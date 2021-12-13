from django.contrib import admin
from clases_abstracta.admin import AbstractaAdmin
from import_export import resources
from .models import Local

class LocalResoucer(resources.ModelResource):
    class Meta:
        model = Local

class LocalAdmin(AbstractaAdmin):
    search_fields = ('nombre', 'direccion')
    list_display = ('nombre', 'direccion', 'contacto', 'estado', 'aforo_maximo')
    list_editable = ('contacto','aforo_maximo')
    resource_class = LocalResoucer

admin.site.register(Local,LocalAdmin)