from django.urls import path
from .views import activosView

app_name = 'activos'

urlpatterns = [
    path('activos/', activosView.as_view(), name = 'activos')

]