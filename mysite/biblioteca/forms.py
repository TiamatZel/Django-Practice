from django import forms
from .models import Resena

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['contenido', 'puntuacion']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu reseña...'}),
            'puntuacion': forms.NumberInput(attrs={'min': 0, 'max': 5}),
        }
