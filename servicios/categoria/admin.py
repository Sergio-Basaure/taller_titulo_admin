from django.contrib import admin
from clases_abstracta.admin import AbstractaAdmin
from .models import CategoriaServicio
from import_export import resources


class CategoriaServicioResource(resources.ModelResource):
    class Meta:
        model = CategoriaServicio

class CategoriaServicioAdmin(AbstractaAdmin):
    search_fields = ('nombre','estado')
    list_display = ('nombre', 'estado')
    resource_class = CategoriaServicioResource

admin.site.register(CategoriaServicio, CategoriaServicioAdmin)
