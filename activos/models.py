from django.db import models

# Create your models here.

class activos(models.Model):
    name_activo = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    num_serie = models.CharField(max_length=10)
    marc_activo = models.CharField(max_length=50)
    plant_activo = models.CharField(max_length=50) 
    area_activo = models.CharField(max_length=100)
    stade_activo = models.CharField(max_length=200)
    value_activo = models.DecimalField(max_digits=10, decimal_places=4, default=0.0, null = True, blank=True)
    date_add = models.DateField()
    life_activo = models.IntegerField(null=True, blank=True)
    last_maintenance = models.DateTimeField(null=True, blank=True)
    guarantee_activo = models.CharField(max_length=40, null=True, blank=True)
    

    