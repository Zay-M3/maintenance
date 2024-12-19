from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class RegisterForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

class employed_mant(forms.Form):
    code = forms.CharField(required=False)
    username = forms.CharField(max_length=250)
    last_name = forms.CharField(max_length=250)
    password1 = forms.CharField(required=False)
    password2 = forms.CharField(required=False)
    area = forms.CharField(max_length=200)
    carge = forms.CharField(max_length=100)
    stade = forms.CharField(max_length=200, required=False)