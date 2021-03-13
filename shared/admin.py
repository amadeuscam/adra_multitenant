from django.contrib import admin

# Register your models here.
from .models import Delegaciones, BeneficiariosGlobales
from django.contrib.auth.decorators import user_passes_test


class BeneficiariosGlobalesAdmin(admin.ModelAdmin):
    list_display = ("nombre_beneficiario", "delegacion_name", "ciudad",)
    list_per_page = 15



admin.site.register(Delegaciones)
admin.site.register(BeneficiariosGlobales,BeneficiariosGlobalesAdmin)
