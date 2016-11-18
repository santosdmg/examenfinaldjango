from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('isbn', 'titulo','imagen','autor','editorial', 'pais','anio',)
