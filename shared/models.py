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
