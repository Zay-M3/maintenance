from django.shortcuts import render
from django.views import View
from .models import activos

# Create your views here.

class activosView(View):
    def get(self, request):
        return render(request, 'activosView.html')
    
class crearActivo(View):
    templete_name = 'crearActivo.html'

    def get(self, request):
        return render(request, self.templete_name)
    
    def post(self, request):
        pass
    
