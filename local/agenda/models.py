from django.db import models
from ..local.models import Local
from cliente.models import Cliente

class Hora(models.Model):
    id = models.AutoField(primary_key = True)
    hora = models.TimeField('Hora', auto_now_add = False, auto_now = False, blank = False, null = False)

    class Meta:
        verbose_name = 'Hora'
        verbose_name_plural = 'Horas'

    def __str__(self) -> str:
        return f'{self.hora}'

class Agenda(models.Model):
    id = models.AutoField(primary_key = True)
    id_local = models.ForeignKey(Local, on_delete = models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    fecha = models.DateField('Fecha', auto_now_add = False, auto_now = False)
    id_hora = models.ForeignKey(Hora, on_delete = models.CASCADE, blank = False, null = False)
    codigo_qr = models.ImageField(upload_to = 'qr', blank = True, null = True)
    estado = models.BooleanField('estado', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True)
    fecha_actualizacion = models.DateField('fecha de actualización', auto_now_add = False, auto_now = True)

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'

    def __str__(self) -> str:
        return f'{self.id}'

    