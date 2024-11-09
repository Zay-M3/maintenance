from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class dashboard(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

class inicio(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'inicio.html')
      
    
