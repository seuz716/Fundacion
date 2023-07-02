from django.db import models

class Servicio(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    # Agrega los campos adicionales necesarios para el modelo

    def __str__(self):
        return self.titulo