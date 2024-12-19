from .models import worker_plant

def empleados_disponibles(request):
    
    empleados = worker_plant.objects.all() 
    return {
        'empleado': empleados 
    }