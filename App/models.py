from django.db import models

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
    
class users(models.Model):
    email = models.CharField(primary_key=True, max_length=100)
    nombre = models.CharField(max_length=100) 
    password = models.CharField(max_length=20)

    def __str__(self):
        return {self.email}


