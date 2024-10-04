from django.contrib import admin
#--->Traemos la Tablas desde MODELS
from .models import *

# Register your models here.
admin.site.register(Users)
admin.site.register(Producto)