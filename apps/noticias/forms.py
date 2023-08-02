from .models import Categorias
from django import forms

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Categorias
        fields = ['nombre']
