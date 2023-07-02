from django.contrib import admin
from .models import InformacionLegal

@admin.register(InformacionLegal)
class InformacionLegalAdmin(admin.ModelAdmin):
    list_display = ('nit', 'representante_legal', 'fecha_constitucion')
    list_filter = ('fecha_constitucion',)
    search_fields = ('nit', 'representante_legal')
    readonly_fields = ('fecha_constitucion',)
    fieldsets = (
        ('Información Básica', {
            'fields': ('nit', 'representante_legal', 'direccion', 'telefono', 'email')
        }),
        ('Detalles', {
            'fields': ('objeto_social', 'registro_dian', 'camara_comercio', 'certificado_esal')
        }),
        ('Fechas', {
            'fields': ('fecha_constitucion',)
        }),
    )
    ordering = ('nit',)

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Si el objeto ya existe (edición)
            return self.readonly_fields + ('nit', 'fecha_constitucion')
        return self.readonly_fields
