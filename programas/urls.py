from django.urls import path
from . import views

app_name = 'programas'

urlpatterns = [
    path('', views.lista_programas, name='lista_programas'),
    path('<int:programa_id>/', views.detalle_programa, name='detalle_programa'),
]
