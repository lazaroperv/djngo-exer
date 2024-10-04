from django.urls import path
#-->Importamos las Vistas para las URL
from .views import *

urlpatterns = [
    #-->URL, FUNCION, NOMBRE PARA HTML
    path('',Home,name='inicio'),
    path('agregar/',Agregar,name='agregar'),
    path('visualizar/',ver_Personajes,name='visualizar'),
    path('modificar/<Codigo>/',Modificar_Personajes,name='modificar'),
    path('eliminar/<Codigo>/',Eliminar_Personajes,name='eliminar'),
    path('logouts/',salir,name='logouts'),
]
