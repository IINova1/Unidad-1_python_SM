from django.db import models
# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    Descripcion = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nombre
    
class zona(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nombre
    
class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    consumo = models.IntegerField()
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    
class medicion(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    consumo = models.IntegerField()

    def __str__(self):
        return f"{self.dispositivo.nombre} - {self.fecha_hora} - {self.consumo}W"
    
class alerta(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha_hora = models.DateTimeField(auto_now_add=True)
    leida = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.dispositivo.nombre} - {self.mensaje[:20]} - {'Leida' if self.leida else 'No Leida'}"