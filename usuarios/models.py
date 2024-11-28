from django.db import models


# Create your models here.

class worker_plant(models.Model):
    code_worker = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    area_worker = models.CharField(max_length=100, null=False)
    carge = models.CharField(max_length=100, null=False)
    stade = models.BooleanField(default=True)
    activo_worker = models.ForeignKey('activos.activos', on_delete=models.SET_NULL, null=True, related_name='activo_trabajador')
    