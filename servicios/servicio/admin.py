from django.contrib import admin
from import_export import resources
from clases_abstracta.admin import AbstractaAdmin
from .models import Servicio



class ServicioResource(resources.ModelResource):
    class Meta:
        model = Servicio

class ServicioAdmin(AbstractaAdmin):
    search_fields = ('nombre', 'id_categoria')
    list_display = ('nombre', 'id_categoria', 'fecha_creacion', 'estado')
    resource_class = ServicioResource

admin.site.register(Servicio, ServicioAdmin)