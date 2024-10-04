#---> Importamos 'FORMS'
from django import forms
#---> Importamos los Modelos/Tablas
from .models import Producto

class NuevoProducto(forms.ModelForm):
    class Meta:
        model = Producto  # Usamos el modelo Producto en lugar de Personaje
        fields = '__all__'  # Se incluyen todos los campos del modelo Producto
