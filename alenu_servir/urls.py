from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Resto de tus importaciones

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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
