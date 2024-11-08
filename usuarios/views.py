from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm

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
                return redirect('inicio')
            else:
                return render(request, self.template_name, {'form' : form, 'error' : ' ✖️ Credenciales incorrectas'})


        return render(request, self.template_name, {'form': form})

class register(View):
    templeate_name = 'login_register/register.html'

    def get(self, request):
        return render(request, self.templeate_name, {
        })

    def post(self, request, *args, **kwargs):
        formregister =  RegisterForm(request.POST)

        if formregister.is_valid():
            username = formregister.cleaned_data['username']
            password1 = formregister.cleaned_data['password1']
            password2 = formregister.cleaned_data['password2']

            if password1 != password2:
                return render(request, self.templeate_name, {
                'error' : ' ✖️ Contraseñas no coinciden'})
            else:
                try:
                    #Creacion y guardar el usuario nuevo
                    user = User.objects.create_user(username=username, password=password1)
                    user.save()
                    #guarda en cookies 
                    login(request, user)
                    return render(request, self.templeate_name, {
                    'usernew' : ' ✔️ Usuario creado con exito'})
                except:
                    return render(request, self.templeate_name, {
                    'error' : ' ✖️ Fallo al crear usuario'})

class singout(View):
    def get(self, request):
        logout(request)
        return redirect('home')
    
