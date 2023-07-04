from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('valores/', views.valores, name='valores'),
    path('signin/', LoginView.as_view(template_name='inicio/signin.html'), name='signin'),

]


    
