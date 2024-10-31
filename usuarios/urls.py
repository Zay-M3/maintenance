from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'usuarios'

urlpatterns = [
    path('home/', dashboard_login.as_view(), name = 'dashboard_login' ),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout')

]
