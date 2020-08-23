from django.contrib import admin
from .models import Service
#en este archivo se debe configurar para que se pueda observar en el panel de administrador
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Service,ServiceAdmin)