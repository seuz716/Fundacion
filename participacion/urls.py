

from django.urls import path
from . import views

app_name = 'participacion'

urlpatterns = [
    path('', views.participacion, name='participacion'),
]
