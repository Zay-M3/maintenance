from django.contrib import admin
from django.urls import path, include
from .views import dashboard, inicio, informes, estadisticas


urlpatterns = [
    path('home/', dashboard.as_view(), name = 'home'),
    path('inicio/', inicio.as_view(), name = 'inicio'),
    path('informes/', informes.as_view(), name = 'informes'),
    path('estadisticas/', estadisticas.as_view(), name = 'estadisticas'),
]