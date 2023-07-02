from django.shortcuts import render
from .models import Contacto

def contacto(request):
    datos_contacto = Contacto.objects.first()
    return render(request, 'contacto/contacto.html', {'datos_contacto': datos_contacto})
