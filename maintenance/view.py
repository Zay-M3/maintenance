from django.views.generic import View, TemplateView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView


class lastView(LoginRequiredMixin, TemplateView):
    template_name = 'lastView.html'

 
class LoginFormView(LoginView):
    template_name =  'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Login'
        return context


    