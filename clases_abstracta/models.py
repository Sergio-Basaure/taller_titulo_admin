from django.db  import models

class AbstrataModelo(models.Model):
    id = models.AutoField(primary_key = True)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)
    fecha_actualizacion = models.DateField('fecha de actualización', auto_now_add = True, auto_now = False)