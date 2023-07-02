from django.db import models

class Programa(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    actividades = models.TextField()

    def __str__(self):
        return self.titulo
