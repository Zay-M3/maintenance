from django.urls import path
from .views import statistics

app_name = 'estadisticas'

urlpatterns = [
    path('estadisticas/', statistics.as_view(), name = 'estadisticas')
]

