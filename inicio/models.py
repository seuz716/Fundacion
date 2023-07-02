from django.db import models

class Inicio(models.Model):
    mision = models.TextField()
    vision = models.TextField()
    objetivo_general = models.TextField()
    objeto_social = models.TextField()
    objetivos_especificos = models.TextField()

    def __str__(self):
        return "Página de Inicio"
