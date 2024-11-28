from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm, employed_mant
from .models import worker_plant
from django.shortcuts import get_object_or_404, redirect

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
                        #stade = True
                        )
                    employed.save()
                    return render(request, self.templeate_name, {   
                    'usernew' : ' ✔️ Usuario creado con exito'})
                except Exception as e:
                    print(e)    
                    return render(request, self.templeate_name, {
                    'error' : ' ✖️ Fallo'})
                
        return render(request, self.templeate_name,{'error' : ' ✖️ Fallo al crear usuario'})
                
class editEmployed(View):
    templete_name = 'empleados/edit_employed.html'

    def get(self, request):
        return render(request, self.templete_name, {
            'categorias' : worker_plant.objects.all()
        })
    
class editEmployed2(View):
    templete_name = 'empleados/edit_employed2.html'

    def get(self, request):
        return render(request, self.templete_name, {
            'code' : 'code'
        } )

def change_status(request, pk):
    empleado = get_object_or_404(worker_plant, pk=pk)
    empleado.stade = False 
    empleado.save()
    return redirect('usuarios:employed')