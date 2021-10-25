from django.db import models

class Contacto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre', max_length = 100, blank = False, null = False)
    email = models.EmailField('Correo Electronico', blank = False, null = False)
    descripcion = models.TextField('Descripcion', max_length = 300,blank = False, null = False)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = True, auto_now_add = False)
    fecha_actualizacion = models.DateField('fecha de actualización', auto_now_add = True, auto_now = False)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self) -> str:
        return self.nombre