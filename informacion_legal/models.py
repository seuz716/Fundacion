from django.db import models

class InformacionLegal(models.Model):
    nit = models.CharField(max_length=20)
    objeto_social = models.TextField()

    def __str__(self):
        return "Información Legal"
