from django.contrib import admin
from clases_abstracta.admin import AbstractaAdmin
from import_export import resources
from .models import Reclamos

class ReclamosResource(resources.ModelResource):
    class Meta:
        model = Reclamos


class ReclamoAdmin(AbstractaAdmin):
    search_fields = ('id_tipo', 'id_local', 'personal_asignado', 'fecha_creacion')
    list_display = ('id_tipo', 'id_local', 'asignado', 'personal_asignado', 'fecha_creacion', 'estado')
    readonly_fields = ('id_tipo', 'id_local', 'descripcion', 'fecha_creacion', 'fecha_actualizacion','asignado')
    list_editable = ('personal_asignado',)
    resource_class = ReclamosResource

    fieldsets =(
        ('Descripción del Reclamo',{
            'fields' : ('id_tipo', 'id_local', 'descripcion', 'fecha_creacion', 'fecha_actualizacion',)
        }),
        ('Administrar reclamo',{
            'classes' : ('wide', 'extrapretty'),
            'fields' : ('asignado', 'personal_asignado','descripcion_personal',)
        })
    )

    def save_model(self, request, obj, form, change) -> None:
        if obj.personal_asignado != None:
            obj.asignado = True
            obj.save()
        else:
            obj.asignado = False
            obj.save()
        return super().save_model(request, obj, form, change)
