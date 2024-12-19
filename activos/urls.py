from django.urls import path
from .views import activosView, crearActivo

app_name = 'activos'

urlpatterns = [
    path('activos/', activosView.as_view(), name = 'activos'),
    path('crear/', crearActivo.as_view(), name = 'crearActivo'),

]