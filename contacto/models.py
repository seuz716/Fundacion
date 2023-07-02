from django.db import models

class Contacto(models.Model):
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    facebook = models.URLField(max_length=200, null=True, blank=True, verbose_name="Facebook")
    instagram = models.URLField(max_length=200, null=True, blank=True, verbose_name="Instagram")
    whatsapp = models.URLField(max_length=200, null=True, blank=True, verbose_name="Whatsapp")
    telegram = models.URLField(max_length=200, null=True, blank=True, verbose_name="Telegram")

    def __str__(self):
        return "Información de Contacto"