from django.contrib import admin
from .models import Categoria, Zona, Dispositivo, Medicion, Alerta

# Register your models here.
admin.site.register([Categoria,Zona])
admin.site.register(Dispositivo)
admin.site.register(Medicion)
admin.site.register(Alerta)