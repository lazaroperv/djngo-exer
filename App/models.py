from django.db import models

# Create your models here.
class Personajes(models.Model):
    Codigo=models.AutoField(primary_key=True)
    Nombre=models.TextField(max_length=30)
    Casa=models.TextField(max_length=15)
    Hechizo=models.TextField(max_length=20)
    Imagen=models.ImageField(upload_to="Personajes",null=True)

    def __int__(self):
        self.Codigo