from django.db import models
from django.contrib.auth.models import User 

class Producto(models.Model):
    codigo = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=100) 
    categoria = models.CharField(max_length=50)  
    descripcion = models.TextField()  
    precio = models.DecimalField(max_digits=10, decimal_places=2)  
    stock = models.IntegerField() 
    imagen = models.ImageField(upload_to="productos", null=True, blank=True) 

    def __str__(self):
        return f"{self.nombre} - {self.categoria}"
    
class Users(models.Model):  # Cambiado a Users siguiendo la convención de nombres de Django
    email = models.CharField(primary_key=True, max_length=100)
    nombre = models.CharField(max_length=100) 
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email  # Método __str__ corregido

class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Asegúrate de que User esté correctamente importado
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Compra de {self.producto.nombre} por {self.usuario.username}"
