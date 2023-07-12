from django import forms
from .models import Asignaturas, Usuarios

class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignaturas
        fields = '__all__'

