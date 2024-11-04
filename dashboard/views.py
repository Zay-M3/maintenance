from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class dashboard(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'home.html')

class task(View):
    def get(self, request):
        return render(request, 'task.html')
     
class inicio(View):
    def get(self, request):
        return render(request, 'inicio.html')
    
class informes(View):
    def get(self, request):
        return render(request, 'informes.html')