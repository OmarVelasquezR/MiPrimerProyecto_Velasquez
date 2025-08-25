from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

# Clase para las recetas
class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    ingredientes = models.JSONField(default=list)
    instrucciones = models.JSONField(default=list)
    imagen = models.ImageField(upload_to='recetas/', blank=True, null=True)
    categorias = models.CharField(max_length=200, blank=True, null=True, help_text="Lista separada por comas")
    alergias = models.CharField(max_length=200, blank=True, null=True, help_text="Lista separada por comas")
    dificultad = models.CharField(max_length=20, choices=[('Fácil', 'Fácil'), ('Intermedio', 'Intermedio'), ('Difícil', 'Difícil')], default='Fácil')
    tiempo = models.PositiveIntegerField(blank=True, null=True, help_text="Tiempo en minutos")
    porciones = models.PositiveIntegerField(blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recetas")
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    # 🔹 Helpers para usar en plantillas
    def categorias_list(self):
        return self.categorias.split(",") if self.categorias else []

    def alergias_list(self):
        return self.alergias.split(",") if self.alergias else []

# Clase para los perfiles de usuario
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares/', blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)
    pais = CountryField(blank_label='(Selecciona un país)', blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    ocupacion = models.CharField(max_length=100, blank=True, null=True)
    sitio_web = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"

# Señales para crear y guardar el perfil de usuario automáticamente    
@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

# Señal para guardar el perfil de usuario automáticamente
@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    instance.perfil.save()
