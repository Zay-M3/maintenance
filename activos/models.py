from django.db import models

# Create your models here.

class activos(models.Model):
    area = models.CharField()
    tipo = models.CharField()
    estado = models.CharField()
    