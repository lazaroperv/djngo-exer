#---> Importamos 'FORMS'
from django import forms
#---> Importamos los Modelos/Tablas
from .models import Producto,users

class NuevoProducto(forms.ModelForm):
    class Meta:
        model = Producto  # Usamos el modelo Producto en lugar de Personaje
        fields = '__all__'  # Se incluyen todos los campos del modelo Producto
        
class NewUser(forms.ModelForm):
    class Meta:
        model = users
        fields = '__all__'
