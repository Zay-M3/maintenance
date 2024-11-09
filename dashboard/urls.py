from django.contrib import admin
from django.urls import path
from .views import dashboard, inicio

app_name = 'dashboard'

urlpatterns = [
    path('home/', dashboard.as_view(), name = 'home'),
    path('inicio/', inicio.as_view(), name = 'inicio'),
]