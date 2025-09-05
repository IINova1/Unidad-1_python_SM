from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción de la categoría.")

    def __str__(self):
        return self.nombre


class Zona(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción de la zona.")

    def __str__(self):
        return self.nombre


class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    consumo_maximo_w = models.IntegerField(help_text="Consumo máximo permitido en Watts.")
    estado = models.BooleanField(default=True, help_text="Indica si el dispositivo está activo.")

    def __str__(self):
        return f"{self.nombre} ({self.zona.nombre})"


# Modelo para registrar el consumo histórico de un dispositivo
class Medicion(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    consumo_w = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Medición de {self.dispositivo.nombre} - {self.consumo_w}W"


# Modelo para registrar alertas cuando el consumo excede el límite
class Alerta(models.Model):
    medicion = models.OneToOneField(Medicion, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)
    revisada = models.BooleanField(default=False, help_text="Indica si la alerta ha sido revisada.")

    def __str__(self):
        return f"Alerta para {self.medicion.dispositivo.nombre}"
