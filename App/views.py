from django.shortcuts import render, get_object_or_404, redirect
# Importamos el Sector de Formularios
from .forms import *
from .models import *
# Importamos la Librería de Logout
from django.contrib.auth import logout
# Importamos la Librería de Permisos
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

# Página principal de la ferretería, mostrando los últimos 3 productos añadidos
def Home(request):
    buscar = Producto.objects.all().order_by('-codigo')[:10]  # Traemos los últimos 3 productos
    data = {
        'productos': buscar
    }
    return render(request, 'index.html', data)

# Ver todos los productos disponibles en la ferretería
def ver_productos(request):
    buscar = Producto.objects.all()  # Traemos todos los productos
    data = {
        'productos': buscar
    }
    return render(request, 'Pages/visualizar.html', data)

# Requiere autenticación y permiso para agregar productos
@login_required
@permission_required('App.add_producto')
def agregar_producto(request):
    data = {
        'form': NuevoProducto()  # Formulario para añadir un nuevo producto
    }
    if request.method == 'POST':
        query = NuevoProducto(data=request.POST, files=request.FILES)
        if query.is_valid():
            query.save()
            data['mensaje'] = "Producto agregado con éxito"
        else:
            data['form'] = NuevoProducto()  # Reinicia el formulario si hay errores
    return render(request, 'Pages/agregar.html', data)

# Modificar un producto existente
@permission_required('App.change_producto')
def modificar_producto(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)  # Busca el producto por código
    data = {
        'form': NuevoProducto(instance=producto)  # Cargamos el formulario con los datos existentes
    }
    if request.method == 'POST':
        query = NuevoProducto(data=request.POST, instance=producto, files=request.FILES)
        if query.is_valid():
            query.save()
            data['mensaje'] = "Producto modificado con éxito"
        else:
            data['form'] = NuevoProducto(instance=producto)  # Reinicia el formulario si hay errores
    return render(request, 'Pages/modificar.html', data)

# Eliminar un producto
@permission_required('App.delete_producto')
def eliminar_producto(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)  # Busca el producto por código
    producto.delete()  # Elimina el producto
    return redirect(to="visualizar")  # Redirige a la página de visualización

# Cerrar sesión
def salir(request):
    logout(request)  # Cierra sesión
    return redirect(to='inicio')  # Redirige a la página de inicio

def Register_user(request):
    
