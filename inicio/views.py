from django.shortcuts import render
from .models import Inicio

def inicio(request):
    # Recuperar los datos del modelo Inicio desde la base de datos
    pagina_inicio = Inicio.objects.first()

    # Pasar los datos a la plantilla utilizando el sistema de renderizado de Django
    return render(request, 'inicio/inicio.html', {'inicio': pagina_inicio})


