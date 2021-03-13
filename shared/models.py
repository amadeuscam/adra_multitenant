from django.db import models
from tenant_schemas.models import TenantMixin


# Create your models here.

class Delegaciones(TenantMixin):
    nombre = models.CharField(max_length=255)
    code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    auto_create_schema = True

    def __str__(self):
        return self.nombre


class BeneficiariosGlobales(models.Model):
    delegacion_name = models.CharField(max_length=350)
    nombre_beneficiario = models.CharField(max_length=250)
    documentacion_beneficiario = models.CharField(max_length=250)
    ciudad = models.CharField(max_length=256)
    provincia = models.CharField(max_length=256)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre_beneficiario
