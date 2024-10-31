from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import LoginForm

    
class dashboard_login(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
           
            return render(request, self.template_name, {'dashboard_content': True})
        else:
            
            form = LoginForm()
            return render(request, self.template_name, {'form': form, 'dashboard_content': False})
        
    def post(self, request, *args,**kwargs):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                login(request, user)
                return redirect('usuarios:dashboard_login')
            else:
                form.add_error(None, 'Usuario o contraseña incorrectos')

        return render(request, self.template_name, {'form': form, 'dashboard_content': False})