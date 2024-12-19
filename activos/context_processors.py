from .models import activos

def activos_list(request):
    activo = activos.objects.all()
    return {
        'activos' : activo
    }