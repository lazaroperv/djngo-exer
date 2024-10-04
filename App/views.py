from django.shortcuts import render, get_object_or_404, redirect
from .forms import *  
from .models import Producto, Compra 
from django.contrib.auth import logout 
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages  # Para mostrar mensajes de error o éxito

# Create your views here.

def Home(request):
    buscar = Producto.objects.all().order_by('-codigo')[:10]  # Traemos los últimos 10 productos
    data = {
        'productos': buscar
    }
    return render(request, 'index.html', data)

def contacto(request):
    return render(request, 'Pages/contacto.html')

def nosotros(request):
    return render(request, 'Pages/nosotros.html')

# Cerrar sesión
def salir(request):
    logout(request)  # Cierra sesión
    return redirect(to='inicio')  # Redirige a la página de inicio

def Register_user(request):
    data = {
        'form': NewUser()  # Formulario para registrar un nuevo usuario
    }
    if request.method == 'POST':
        query = NewUser(data=request.POST)
        if query.is_valid():
            query.save()
            data['mensaje'] = "Se ha registrado correctamente"
        else:
            data['form'] = query  # Mantener el formulario con errores
    return render(request, 'Pages/register_user.html', data)

def comprar_producto(request, producto_id):
    producto = get_object_or_404(Producto, codigo=producto_id)  # Busca el producto por código

    # Simulamos la compra verificando el stock disponible
    if producto.stock > 0:
        producto.stock -= 1  
        producto.save()  

        # Crear la compra
        compra = Compra.objects.create(
            usuario=request.user,  # Usuario autenticado
            producto=producto,    
            cantidad=1,          
            precio_total=producto.precio  # El precio total es igual al precio del producto
        )
        compra.save()  # Guardar la compra en la base de datos

        messages.success(request, f"Has comprado {producto.nombre} con éxito.")
        return render(request, 'Pages/confirmacion_compra.html', {'producto': producto})

    else:
        messages.error(request, f"Lo siento, no hay stock disponible para {producto.nombre}.")
        return render(request, 'Pages/sin_stock.html', {'producto': producto})
