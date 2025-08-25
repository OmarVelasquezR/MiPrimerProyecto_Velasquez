from django.contrib import admin
from .models import Receta

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'creado', 'actualizado')
    list_filter = ('creado', 'actualizado', 'dificultad', 'categorias')
    search_fields = ('titulo', 'descripcion', 'ingredientes')
    ordering = ('-creado',)
