from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import loginUser, register, singout

app_name = 'usuarios'

urlpatterns = [
    path('login/', loginUser.as_view(), name = 'login'),
    path('register/', register.as_view(), name = 'register'),
    path('logaut/', singout.as_view(), name = 'logaut')
    
]
