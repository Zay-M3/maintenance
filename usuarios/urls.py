
from django.urls import path
from .views import loginUser, register, singout, create_user_mant, editEmployed
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', loginUser.as_view(), name = 'login'),
    path('register/', register.as_view(), name = 'register'),
    path('logaut/', singout.as_view(), name = 'logaut'),
    path('create/user/', create_user_mant.as_view(), name = 'createemployed'),
    path('empleado/', editEmployed.as_view(), name = 'employed'),
    path('change_status/<int:pk>/', views.change_status, name='change_status'),
]
