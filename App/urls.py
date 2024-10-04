from django.urls import path
#--> Importamos las Vistas para las URL
from .views import *

urlpatterns = [
    #--> URL, FUNCIÓN, NOMBRE PARA HTML
    path('', Home, name='inicio'),  # Página de inicio
    path('agregar/', agregar_producto, name='agregar'),  # Agregar producto
    path('visualizar/', ver_productos, name='visualizar'),  # Visualizar productos
    path('modificar/<int:codigo>/', modificar_producto, name='modificar'),  # Modificar producto
    path('eliminar/<int:codigo>/', eliminar_producto, name='eliminar'),  # Eliminar producto
    path('logouts/', salir, name='logouts'),  # Cerrar sesión
    path('Register_user/', Register_user,name="Register_user"),
]
