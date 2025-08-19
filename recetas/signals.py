from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Perfil

@receiver(post_save, sender=User)
def crear_o_actualizar_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        # Solo crear el perfil si no existe
        if not hasattr(instance, 'perfil'):
            Perfil.objects.create(usuario=instance)
    else:
        # Solo guardar si el perfil ya existe
        try:
            instance.perfil.save()
        except Perfil.DoesNotExist:
            Perfil.objects.create(usuario=instance)
