from django.shortcuts import render, get_object_or_404
from .models import Servicio

def lista_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios/lista_servicios.html', {'servicios': servicios})

def detalle_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    return render(request, 'servicios/detalle_servicio.html', {'servicio': servicio})
