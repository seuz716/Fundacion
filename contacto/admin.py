from django.contrib import admin
from .models import Contacto

class ContactoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contacto, ContactoAdmin)
