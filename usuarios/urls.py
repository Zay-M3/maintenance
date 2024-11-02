from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import dashboard, loginUser

app_name = 'usuarios'

urlpatterns = [
    path('login/', loginUser.as_view(), name = 'login'),
    path('home/', dashboard.as_view(), name = 'home' ),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout')
    

]
