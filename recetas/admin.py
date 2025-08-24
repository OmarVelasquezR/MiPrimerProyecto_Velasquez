from django.contrib import admin
from .models import Receta

# Admin para gestionar las recetas
@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion')
    search_fields = ('titulo', 'ingredientes')
    list_filter = ('fecha_creacion',)
    ordering = ('-fecha_creacion',)
