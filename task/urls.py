from django.urls import path
from .views import tasks

app_name = 'task'

urlpatterns = [
    path('tareas/', tasks.as_view(), name = 'tareas'),
]