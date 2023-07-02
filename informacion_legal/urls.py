from django.urls import path
from . import views

app_name = 'informacion_legal'

urlpatterns = [
    path('', views.informacion_legal, name='informacion_legal'),
]
