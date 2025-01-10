from django.shortcuts import render
from django.views import View
from .models import activos
from .forms import activosForms

# Create your views here.

class activosView(View):
    def get(self, request):
        return render(request, 'activosView.html')
    
class crearActivo(View):
    templete_name = 'crearActivo.html'

    def get(self, request):
        return render(request, self.templete_name)
    
    def post(self, request, *args, **kwargs):
        formActivocreate = activosForms(request.POST)

        if formActivocreate.is_valid():
            codigoActivo = formActivocreate.cleaned_data['code_activo']
            nombreActivo = formActivocreate.cleaned_data['name_activo']
            numeroSerie = formActivocreate.cleaned_data['num_serie']
            marcaActivo = formActivocreate.cleaned_data['marc_activo']
            valorActivo = formActivocreate.cleaned_data['value_activo']
            garantiaActivo = formActivocreate.cleaned_data['guarantee_activo_time']
            areaActivo = formActivocreate.cleaned_data['area_activo']
            estadoActivo = formActivocreate.cleaned_data['stade_activo']

            if not isinstance(codigoActivo, int):
                return render(request, self.templete_name, {
                'error' : ' ✖️ El codigo debe ser un numero'})
            if not isinstance(numeroSerie, int):
                return render(request, self.templete_name, {
                'error' : ' ✖️ El numero de serie debe ser un numero'})
            if not isinstance(valorActivo, int):
                return render(request, self.templete_name, {
                'error' : ' ✖️ El valor debe ser de tipo numerico'})
            else: 
                try:
                    activo = activos.objects.create(
                        codigoActivo = codigoActivo,
                        nombreActivo = nombreActivo,
                        numeroSerie = numeroSerie,
                        marcaActivo = marcaActivo,
                        areaActivo = areaActivo,
                        estadoActivo = estadoActivo, 
                        valorActivo = valorActivo,
                        garantiaActivoTiempo = garantiaActivo
                    )
                    activo.save()
                    return render(request, self.templete_name, {   
                    'usernew' : ' ✔️ Usuario creado con exito'})
                except Exception as e:
                    print(e)    
                    return render(request, self.templete_name, {
                    'error' : ' ✖️ Fallo'})
        else:
            print(formActivocreate.errors)
        return render(request, self.templete_name,{'error' : ' ✖️ Fallo al crear usuario'})
            
    
