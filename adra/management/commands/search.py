from django.core.management.base import BaseCommand, CommandError
from datetime import date
from adra.models import Persona,Alimentos
from tenant_schemas.management.commands import BaseTenantCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        persona = Persona.objects.all()
        today = date.today()
        for p in persona:
            print(p.numero_adra)
            # print( today.year - p.fecha_nacimiento.year - ((today.month, today.day) < (p.fecha_nacimiento.month, p.fecha_nacimiento.day)))
