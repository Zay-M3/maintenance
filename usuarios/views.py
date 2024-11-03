from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm

    
class dashboard(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'home.html')

class loginUser(View):
    template_name = 'login_register/login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form' : form })

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
                return render(request, self.template_name, {'form' : form, 'error' : ' ✖️ Credenciales incorrectas'})


        return render(request, self.template_name, {'form': form})

class register(View):
    def get(self, request):
        return render(request, 'login_register/register.html', {
        })
    
    def post(self, request, *args, **kwargs):
        formregister =  RegisterForm(request.POST)

        if formregister.is_valid():
            username = formregister.cleaned_data['username']
            password1 = formregister.cleaned_data['password1']
            password2 = formregister.cleaned_data['password2']

            if password1 == password2:
                try:
                    user = User.objects.create_user(username=username, password=password1)
                    user.save()
                    return render(request, 'login_register/register.html', {
                    'usernew' : ' ✔️ Usuario creado con exito'})
                except:
                    return render(request, 'login_register/register.html', {
                    'error' : ' ✖️ Fallo al crear usuario'})
            else:
                return render(request, 'login_register/register.html', {
                'error' : ' ✖️ Contraseñas no coinciden'})

