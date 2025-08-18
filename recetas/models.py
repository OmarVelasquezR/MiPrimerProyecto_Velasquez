from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Clase para las recetas
class Receta(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    imagen = models.ImageField(upload_to='recetas/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titulo

# Clase para los perfiles de usuario
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares/', blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    ocupacion = models.CharField(max_length=100, blank=True, null=True)
    sitio_web = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"
    
@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    instance.perfil.save()
