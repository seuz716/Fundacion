from django.shortcuts import render, get_object_or_404
from .models import Programa

def lista_programas(request):
    programas = Programa.objects.all()
    return render(request, 'programas/lista_programas.html', {'programas': programas})

def detalle_programa(request, programa_id):
    programa = get_object_or_404(Programa, pk=programa_id)
    return render(request, 'programas/detalle_programa.html', {'programa': programa})
