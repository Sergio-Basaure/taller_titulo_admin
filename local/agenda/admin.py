from django.contrib import admin
from import_export import resources
from clases_abstracta.admin import AbstractaAdmin
from .models import Agenda,Hora

class AgendaResoucer(resources.ModelResource):
    class Meta:
        model = Agenda

class AgendaAdmin(AbstractaAdmin):
    resource_class = AgendaResoucer

class HoraResource(resources.ModelResource):
    class Meta:
        model = Hora

class HoraAdmin(AbstractaAdmin):
    resource_class = HoraResource

admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Hora, HoraAdmin)