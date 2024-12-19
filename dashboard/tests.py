from django.test import TestCase
from usuarios.models import worker_plant

# Create your tests here.


empleados = worker_plant.objects.all()
print(empleados)