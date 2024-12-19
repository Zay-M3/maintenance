from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm, employed_mant
from .models import worker_plant
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.hashers import make_password

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
                return redirect('dashboard:inicio')
            else:
                return render(request, self.template_name, {'form' : form, 'error' : ' ✖️ Credenciales incorrectas'})


        return render(request, self.template_name, {'form': form})

   
class singout(View):
    def get(self, request):
        logout(request)
        return redirect('usuarios:login')
    
#Empleados

class create_user_mant(LoginRequiredMixin, View):
    templeate_name = 'empleados/user_mant.html'
    
    def get(self, request):
        return render(request, self.templeate_name) 
    
    def post(self, request, *args, **kwargs):
        formsemployed =  employed_mant(request.POST)

        print(formsemployed.is_valid())

        if formsemployed.is_valid():
            code = formsemployed.cleaned_data['code']
            username = formsemployed.cleaned_data['username']
            last_name  = formsemployed.cleaned_data['last_name']
            password1 = formsemployed.cleaned_data['password1']
            password2 = formsemployed.cleaned_data['password2']
            area = formsemployed.cleaned_data['area']
            carge = formsemployed.cleaned_data['carge']

            if password1 != password2:
                return render(request, self.templeate_name, {
                'error' : ' ✖️ Contraseñas no coinciden'})
            else:
                try:
                    user = User.objects.create_user(username=username, password=password1)
                    user.save()
                    employed = worker_plant.objects.create(
                        code_worker = code,
                        name = username,
                        last_name =last_name,
                        area_worker = area,
                        carge = carge,
                        activo_worker = None,
                        password = password1,
                        stade = 'Activo'
                        )
                    employed.save()
                    return render(request, self.templeate_name, {   
                    'usernew' : ' ✔️ Usuario creado con exito'})
                except Exception as e:
                    print(e)    
                    return render(request, self.templeate_name, {
                    'error' : ' ✖️ Fallo'})
        else:
            print(formsemployed.errors)
        return render(request, self.templeate_name,{'error' : ' ✖️ Fallo al crear usuario'})
                
class editEmployed(View):
    templete_name = 'empleados/edit_employed.html'

    def get(self, request):
        return render(request, self.templete_name, {
            'categorias' : worker_plant.objects.all()
        })
    
class change_status(View):
    
    def get(self, request, pk):
        empleado = get_object_or_404(worker_plant, pk = pk)
        print(pk)
        empleado.stade = 'Inactivo'
        empleado.save()
        return redirect('usuarios:employed')
    
class edit_employed(View):
    templete_name = 'empleados/edit_employed2.html' 

    def get(self, request, pk):
        print(pk)
        return render(request, self.templete_name, {
           'empleado' : worker_plant.objects.filter(pk = pk)
        })
    
    def post(self, request, pk, *args, **kwargs):
        employedsave = get_object_or_404(worker_plant, pk=pk)
        formemployedsave =  employed_mant(request.POST)
        
        print("hello")
        print(formemployedsave.is_valid())
        if formemployedsave.is_valid():
            password1 = formemployedsave.cleaned_data['password1']
            password2 = formemployedsave.cleaned_data['password2']
            print("hola")
            if password1 != password2:
                return render(request, self.templete_name, {
                'error' : ' ✖️ Contraseñas no coinciden'})
            else:
                try:
                    print("hola")
                    employedsave.name = formemployedsave.cleaned_data['username']
                    employedsave.last_name = formemployedsave.cleaned_data['last_name']
                    employedsave.password = make_password(formemployedsave.cleaned_data['password1'])
                    employedsave.stade = formemployedsave.cleaned_data['stade']
                    employedsave.carge = formemployedsave.cleaned_data['carge']
                    employedsave.area_worker = formemployedsave.cleaned_data['area']
                    employedsave.save()
                    return redirect('usuarios:employed')
                except Exception as e:
                    print(e)
                    return render(request, self.templete_name, {
                    'error' : ' ✖️ Fallo'})    
        return render(request, self.templete_name,{'error' : ' ✖️ Fallo al guardar el usuario'})