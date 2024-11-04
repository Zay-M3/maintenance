from django.contrib import admin
from django.urls import path
from .views import dashboard, task, inicio, informes


urlpatterns = [
    path('home/', dashboard.as_view(), name = 'home'),
    path('tareas/', task.as_view(), name = 'tareas'),
    path('inicio/', inicio.as_view(), name = 'inicio'),
    path('informes/', informes.as_view(), name = 'informes'),
]