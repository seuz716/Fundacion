from django.db import models

class InformacionLegal(models.Model):
    nit = models.CharField(max_length=20)
    objeto_social = models.TextField()
    representante_legal = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100, default='')
    telefono = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    fecha_constitucion = models.DateField(null=True)
    registro_dian = models.CharField(max_length=100)
    camara_comercio = models.CharField(max_length=100, default='')
    certificado_esal = models.FileField(upload_to='esal_certificates/', default=None)

    def __str__(self):
        return "Información Legal"
