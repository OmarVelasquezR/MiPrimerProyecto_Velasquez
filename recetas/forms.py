from django import forms
from .models import Receta
from .models import Perfil
from django_countries.widgets import CountrySelectWidget


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'descripcion', 'ingredientes', 'instrucciones', 'imagen']
        widgets = {
            'descripcion': forms.Textarea(attrs={
                'placeholder': 'Ejemplo: Delicioso pollo al horno con vegetales...',
                'rows': 3
            }),
            'ingredientes': forms.Textarea(attrs={
                'placeholder': 'Ejemplo:\nPollo\nTomate\nSal\nZanahoria',
                'rows': 8
            }),
            'instrucciones': forms.Textarea(attrs={
                'placeholder': 'Ejemplo:\nPreparar los ingredientes\nCocinar el pollo...',
                'rows': 8
            }),
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