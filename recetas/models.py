from django.db import models
from django.utils import timezone

class Receta(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    imagen = models.ImageField(upload_to='recetas/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
