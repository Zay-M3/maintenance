
from django.urls import path
from .views import loginUser, singout, create_user_mant, edit_employed, editEmployed, change_status
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', loginUser.as_view(), name = 'login'),
    path('logaut/', singout.as_view(), name = 'logaut'),
    path('employed/', editEmployed.as_view(), name ='employed' ),
    path('create/user/', create_user_mant.as_view(), name = 'createemployed'),
    path('change_status/<int:pk>/', change_status.as_view(), name='change_status'),
    path('edit/employed/<int:pk>/', edit_employed.as_view(), name='edit_employed')
]
