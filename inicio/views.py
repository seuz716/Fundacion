from .models import Inicio
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect

def inicio(request):
    # Recuperar los datos del modelo Inicio desde la base de datos
    pagina_inicio = Inicio.objects.first()

    # Pasar los datos a la plantilla utilizando el sistema de renderizado de Django
    return render(request, 'inicio/inicio.html', {'inicio': pagina_inicio})



def signup(request):
    if request.method == 'POST':
        try:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                # Realizar acciones adicionales después del registro exitoso
                messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
                return redirect('inicio:inicio')  # Redirigir a la URL nombrada 'inicio:inicio'
        except Exception as e:
            messages.error(request, 'Ocurrió un error durante el registro: {}'.format(str(e)))
    else:
        form = UserCreationForm()
    
    return render(request, 'inicio/signup.html', {'form': form})



def valores(request):
    inicio = Inicio.objects.first()  # Recupera los datos del modelo Inicio desde la base de datos
    return render(request, 'inicio/valores.html', {'inicio': inicio})

