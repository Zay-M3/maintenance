from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class worker_plant(models.Model):
    code_worker = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    area_worker = models.CharField(max_length=100, null=False)
    carge = models.CharField(max_length=100, null=False)
    stade = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    activo_worker = models.ForeignKey('activos.activos', on_delete=models.SET_NULL, null=True, related_name='activo_trabajador')
    