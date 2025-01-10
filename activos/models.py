from django.db import models

# Create your models here.

class activos(models.Model):
    codigoActivo = models.BigIntegerField(unique=True)
    nombreActivo = models.CharField(max_length=200)
    categoriaActivo = models.CharField(max_length=200)
    numeroSerie = models.CharField(max_length=10)
    marcaActivo = models.CharField(max_length=50)
    areaActivo = models.CharField(max_length=100)
    estadoActivo = models.CharField(max_length=200)
    valorActivo = models.DecimalField(max_digits=10, decimal_places=4, default=0.0, null = True, blank=True)
    fechaRegistro = models.DateField(auto_now_add=True)
    ultimoMantenimiento = models.DateTimeField(null=True, blank=True)
    garantiaActivoTiempo = models.CharField(max_length=200)
    

    