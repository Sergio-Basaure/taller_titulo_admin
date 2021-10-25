from django.contrib import admin
from clases_abstracta.admin import AbstractaAdmin
from import_export import resources
from .models import TipoReclamo

class TipoReclamoResource(resources.ModelResource):
    class Meta:
        model = TipoReclamo

class TipoReclamoAdmin(AbstractaAdmin):
    search_fields = ('nombre',)
    list_display = ('nombre', 'estado')
    resource_class = TipoReclamoResource

admin.site.register(TipoReclamo, TipoReclamoAdmin)