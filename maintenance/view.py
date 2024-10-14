from django.views.generic import View
from django.shortcuts import render

class HomeView(View):
    def get(self, request, *arg, **kwargs):
        context = {
            
        }

        return render(request, "index.html", context)