from django import forms
from .models import Receta, Perfil
from django_countries.widgets import CountrySelectWidget

# Formulario para crear o editar una receta
class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = [
            'titulo', 'descripcion', 'imagen',
            'categorias', 'alergias', 'dificultad',
            'tiempo', 'porciones', 'ingredientes', 'instrucciones'
        ]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'categorias': forms.TextInput(attrs={'class': 'form-control'}),
            'alergias': forms.TextInput(attrs={'class': 'form-control'}),
            'dificultad': forms.Select(attrs={'class': 'form-select'}),
            'tiempo': forms.NumberInput(attrs={'class': 'form-control'}),
            'porciones': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# Formulario para editar el perfil de usuario
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'avatar', 'biografia', 'ciudad', 'pais', 'telefono',
            'fecha_nacimiento', 'ocupacion', 'sitio_web',
            'instagram', 'facebook', 'twitter'
        ]
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'pais': CountrySelectWidget(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
        
        self.fields['avatar'].label = "Foto de perfil"

        avatar_field = self.fields.get('avatar')
        if avatar_field and hasattr(avatar_field.widget, 'clear_checkbox_label'):
            avatar_field.widget.clear_checkbox_label = "Eliminar imagen"
            avatar_field.widget.initial_text = "Imagen actual"
            avatar_field.widget.input_text = "Cambiar"