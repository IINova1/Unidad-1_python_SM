from django.db import models
# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    Descripcion = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nombre
    


class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    consumo = models.IntegerField()
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre