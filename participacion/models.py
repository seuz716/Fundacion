from django.db import models

class Participacion(models.Model):
    opciones_participacion = (
        ('voluntariado', 'Voluntariado'),
        ('patrocinio', 'Patrocinio de programas'),
        ('colaboracion', 'Colaboración en eventos y actividades'),
    )
    tipo_participacion = models.CharField(max_length=20, choices=opciones_participacion)
    descripcion = models.TextField()

    def __str__(self):
        return "Participación"
