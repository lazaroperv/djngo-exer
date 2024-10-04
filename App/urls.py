from django.urls import path
#--> Importamos las Vistas para las URL
from .views import *

urlpatterns = [
    #--> URL, FUNCIÓN, NOMBRE PARA HTML
    path('', Home, name='inicio'),  # Página de inicio
    path('logouts/', salir, name='logouts'),  # Cerrar sesión
    path('Register_user/', Register_user,name="Register_user"),
    path('comprar/<int:producto_id>/',comprar_producto, name='comprar'),
    path('contacto/', contacto,name="contacto"),
    path('nosotros/', nosotros,name="nosotros"),


]
