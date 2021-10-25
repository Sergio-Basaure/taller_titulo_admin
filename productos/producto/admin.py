from django.contrib import admin
from .models import Producto
from clases_abstracta.admin import AbstractaAdmin
from import_export import resources

class ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto

class ProductoAdmin(AbstractaAdmin):
    search_fields = ('nombre', 'marca', 'id_categoria')
    list_display = ('nombre', 'marca', 'id_categoria', 'estado', 'stock', 'fecha_actualizacion')
    list_editable = ('stock',)
    resource_class = ProductoResource


    def save_model(self, request, obj, form, change) -> None:
        if obj.stock == 0:
            obj.estado = False
            obj.save()
        else:
            obj.estado = True
            obj.save()
        return super().save_model(request, obj, form, change)


admin.site.register(Producto, ProductoAdmin)