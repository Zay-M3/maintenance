from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import LoginForm

    
class dashboard(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'home.html')

class loginUser(View):
    template_name = 'login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form' : form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
        
            if user is not None:
                login(request, user)
                return redirect('/usuarios/home/')
            else:
                form.add_error(None, 'Usuario no encontrado')


        return render(request, self.template_name, {'form': form})
