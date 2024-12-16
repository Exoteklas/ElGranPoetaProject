from django.db import models
from django.contrib.auth.models import User, Group
#Create your models here.

class AuditLog(models.Model):
    user = models.CharField(max_length=255)  # Nombre del usuario
    group = models.CharField(max_length=255)  # Nombre del grupo
    action = models.CharField(max_length=255)  # e.g. "Creación", "Actualización", "Eliminación"
    model_name = models.CharField(max_length=255)  # El nombre del modelo que se modificó
    timestamp = models.DateTimeField(auto_now_add=True)  # Hora del cambio

    def __str__(self):
        return f"{self.timestamp} - {self.action} - {self.model_name} por {self.user} (ID: {self.id})"


class Autor(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)
     # Añade registro histórico

    def __str__(self):
        return self.nombre


class Bodega(models.Model):
    ubicacion = models.CharField(max_length=255)


    def __str__(self):
        return f"Bodega {self.id} - {self.ubicacion}"


class Libro(models.Model):
    nombre_libro = models.CharField(max_length=255)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)  # Relación con Autor
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)  # Relación con Bodega
    stock = models.IntegerField()
    fecha_publicacion = models.DateField()
    descripcion = models.CharField(max_length=255)
     # Para registrar historial

    def __str__(self):
        return self.nombre_libro