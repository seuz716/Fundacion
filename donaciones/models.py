from django.db import models

class Donacion(models.Model):
    opciones_donacion = (
        ('efectivo', 'Donación en efectivo'),
        ('bonos', 'Donación de bonos'),
        ('transferencia', 'Transferencia bancaria'),
    )
    tipo_donacion = models.CharField(max_length=20, choices=opciones_donacion)
    descripcion = models.TextField()

    def __str__(self):
        return "Donaciones"
