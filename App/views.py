from django.shortcuts import render, get_object_or_404, redirect
from .forms import *  # Asegúrate de que tienes los formularios correctamente definidos
from .models import Producto, Compra  # Importación de tus modelos
from django.contrib.auth import logout  # Importamos la Librería de Logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages  # Para mostrar mensajes de error o éxito

# Create your views here.

# Página principal de la ferretería, mostrando los últimos 10 productos añadidos
def Home(request):
    buscar = Producto.objects.all().order_by('-codigo')[:10]  # Traemos los últimos 10 productos
    data = {
        'productos': buscar
    }
    return render(request, 'index.html', data)

def contacto(request):
    return render(request,'Pages/contacto.html')
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
            data['form'] = query  # Mantener el formulario con errores
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
            data['form'] = query  # Mantener el formulario con errores
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
        producto.stock -= 1  # Reducir el stock en 1
        producto.save()  # Guardar cambios en el producto

        # Crear la compra
        compra = Compra.objects.create(
            usuario=request.user,  # Usuario autenticado
            producto=producto,     # Producto comprado
             cantidad=1,            # Por ahora, 1 unidad
            precio_total=producto.precio  # El precio total es igual al precio del producto
        )
        compra.save()  # Guardar la compra en la base de datos

        # Mostrar un mensaje de éxito y redirigir a una página de confirmación
        messages.success(request, f"Has comprado {producto.nombre} con éxito.")
        return render(request, 'Pages/confirmacion_compra.html', {'producto': producto})

    # Si no hay stock disponible, mostramos un mensaje de error
    else:
        messages.error(request, f"Lo siento, no hay stock disponible para {producto.nombre}.")
        return render(request, 'Pages/sin_stock.html', {'producto': producto})
