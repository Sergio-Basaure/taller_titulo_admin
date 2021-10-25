from django.contrib import admin
from clases_abstracta.admin import AbstractaAdmin
from import_export import resources
from .models import Cliente

class ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente

class ClienteAdmin(AbstractaAdmin):
    
    search_fields = ('nombres', 'apellidos', 'rut', 'email')
    list_display = ('nombres', 'apellidos', 'rut', 'email','contacto', 'estado')
    exclude = ('password', 'last_login', 'fecha_actualizacion', 'estado')
    readonly_fields = ('fecha_creacion','nombres', 'apellidos', 'rut', 'email', 'contacto',)
    resource_class = ClienteResource

admin.site.register(Cliente, ClienteAdmin)