import csv
import os
from django.core.files import File
from django.conf import settings
import django
import sys

sys.path.append('/home/aguero/djngo-exer')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Proyecto.settings')
django.setup()

from App.models import Producto
ruta = '/home/aguero/djngo-exer/productos_ferreteria.csv'

if os.path.exists(ruta):
    with open(ruta, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            producto = Producto(
                nombre=row['nombre'],
                categoria=row['categoria'],
                descripcion=row['descripcion'],
                precio=row['precio'],
                stock=row['stock'],
                imagen=f'productos/{row["imagen"]}'
            )
            producto.save()
            print(f'Producto agregado: {producto.nombre}')
else:
    print("El archivo no existe en la ruta especificada.")
