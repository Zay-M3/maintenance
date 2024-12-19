from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class dashboard(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        
        return render(request, 'home.html')

class inicio(LoginRequiredMixin, View):
    def get(self, request):
        
        return render(request, 'inicio.html')
      
    
