from django.contrib.auth import authenticate
from .models import Inicio
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
import logging
from .forms import SignInForm
from django.core.exceptions import ValidationError
from django import forms

def inicio(request):
    # Recuperar los datos del modelo Inicio desde la base de datos
    pagina_inicio = Inicio.objects.first()

    # Pasar los datos a la plantilla utilizando el sistema de renderizado de Django
    return render(request, 'inicio/inicio.html', {'inicio': pagina_inicio})


def signup(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, 'inicio/signup.html', {'form': form})
    
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
                return redirect('inicio:inicio')
            except IntegrityError:
                messages.error(request, 'El nombre de usuario o la dirección de correo electrónico ya están en uso.')
            except Exception as e:
                messages.error(request, 'Ocurrió un error durante el registro: {}'.format(str(e)))
    
    else:
        form = UserCreationForm()
    
    return render(request, 'inicio/signup.html', {'form': form})



class SignInForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

def signin(request):
    if request.method == "GET":
        form = SignInForm()
        return render(request, 'inicio/signin.html', {'form': form})
    elif request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio:inicio')  # Redirige a la página de inicio después del inicio de sesión exitoso
            else:
                error = 'Usuario o contraseña incorrectos'
        else:
            error = 'Formulario no válido'
        
        context = {'form': form, 'error': error}
        return render(request, 'inicio/signin.html', context)
    else:
        form = SignInForm()
        context = {'form': form}
        return render(request, 'inicio/signin.html', context)

def signout(request):
    try:
        logout(request)
    except PermissionDenied as e:
        logger.error(f"Permiso denegado al cerrar sesión: {str(e)}")
    except ObjectDoesNotExist as e:
        logger.error(f"Objeto no existe al cerrar sesión: {str(e)}")
    except Exception as e:
        logger.error(f"Error ocurrido durante el cierre de sesión: {str(e)}")
    
    return redirect('inicio:inicio')



def valores(request):
    inicio = Inicio.objects.first()  # Recupera los datos del modelo Inicio desde la base de datos
    return render(request, 'inicio/valores.html', {'inicio': inicio})

