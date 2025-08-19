from django.apps import AppConfig

# Configuración de la señal para crear y guardar el perfil de usuario
class RecetasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recetas'

    def ready(self):
        import recetas.signals
