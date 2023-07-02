from django.db import models

class Contacto(models.Model):
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return "Información de Contacto"
