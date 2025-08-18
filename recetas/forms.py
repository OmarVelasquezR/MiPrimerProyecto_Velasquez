from django import forms
from .models import Receta

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
