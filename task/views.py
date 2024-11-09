from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class tasks(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'task.html')