from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Contacto

@admin.action(description='Eliminación lógica')
def eliminacion_logica(modeladmin, request, queryset):
    for obj in queryset:
        obj.estado = False
        obj.save()

@admin.action(description='Activación lógica')
def activacion_logica(modeladmin, request, queryset):
    for obj in queryset:
        obj.estado = True
        obj.save()


class ContactoResource(resources.ModelResource):
    class Meta:
        model = Contacto


class ContactoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ('email', 'nombre')
    list_display = ('nombre', 'email', 'fecha_creacion', 'estado')
    readonly_fields = ('nombre', 'email', 'descripcion')
    search_fields = ('nombre', 'email')
    resource_class = ContactoResource

    actions = [eliminacion_logica, activacion_logica]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def delete_model(self, request, obj):
        obj.estado = False
        obj.save()
        return (request, obj)

admin.site.register(Contacto, ContactoAdmin)