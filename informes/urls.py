from django.urls import path
from .views import informes

app_name = 'informes'

urlpatterns = [
    path('informes/', informes.as_view(), name = 'informes')
]