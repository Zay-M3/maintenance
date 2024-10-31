from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Usuario/Correo')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')