from django.db import models

# Create your models here.

class report_maintenance(models.Model):
    #Para reporte de mantenimiento
    worker = models.CharField(max_length=200)
    activo = models.CharField(max_length=200)
    code = models.IntegerField()
    area_plant = models.CharField(max_length=200, null= True, blank=True)
    area_office = models.CharField(max_length=200, null= True, blank=True)
    area_building = models.CharField(max_length=200, null= True, blank=True)
    mant_equipment = models.BooleanField(default=False)
    mant_corrective = models.BooleanField(default=False)
    mant_infrastructure = models.BooleanField(default=False)
    mant_mejore = models.BooleanField(default=False)
    description = models.TextField()
    date_iniciate = models.DateTimeField()
    #Area mantenimiento
    mant_mecanic = models.BooleanField(default=False)
    mant_electric = models.BooleanField(default=False)
    mant_other = models.BooleanField(default=False)
    worker_mant = models.CharField(max_length=200)
    date_finish = models.DateTimeField()
    recomendations = models.TextField()
    time_respont = models.CharField(max_length=200)