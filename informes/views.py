from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import report_maintenance
from usuarios.models import worker_plant

# Create your views here.

class informes(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'informes.html')
    
    def post(self, request):  
        pass 

