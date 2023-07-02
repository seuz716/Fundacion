from django.shortcuts import render
from .models import InformacionLegal

def informacion_legal(request):
    datos_informacion_legal = InformacionLegal.objects.first()
    return render(request, 'informacion_legal/informacion_legal.html', {'datos_informacion_legal': datos_informacion_legal})
