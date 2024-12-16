from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TicketSoporte(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('resuelto', 'Resuelto'),
        ('cerrado', 'Cerrado'),
    ]
    
    PRIORIDAD_CHOICES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tickets")
    asunto = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, default='media')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_resolucion = models.DateTimeField(null=True, blank=True)
    observacion = models.TextField(null=True)