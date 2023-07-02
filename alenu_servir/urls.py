from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('contacto/', include('contacto.urls')),
    path('informacion_legal/', include('informacion_legal.urls')),
    path('programas/', include('programas.urls')),
    path('servicios/', include('servicios.urls')),
    path('donaciones/', include('donaciones.urls')),
    path('participacion/', include('participacion.urls')),
]

