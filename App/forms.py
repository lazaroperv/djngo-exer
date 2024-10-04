#--->Importamos 'FORMS'
from django import forms
#---> Importamos los Modelos/Tablas
from .models import *

class NuevoPersonaje(forms.ModelForm):
    class Meta:
        model=Personajes
        fields='__all__'