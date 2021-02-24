from django.core.management.base import BaseCommand, CommandError
from datetime import date
from adra.models import AlmacenAlimentos, Persona
from django.db.models import Count
from django.contrib.auth.models import User
from adra.models import Persona, Alimentos, Hijo
from tenant_schemas.utils import get_tenant_model, tenant_context
from django.db import connection
import sendgrid

from django.conf import settings

class Command(BaseCommand):

    def handle(self, *args, **options):
        list_email = None
        for tenant in get_tenant_model().objects.exclude(schema_name='public'):
            with tenant_context(tenant):
                print(tenant)
                ali = AlmacenAlimentos.objects.all()
                emails = User.objects.filter(is_active=True, is_staff=True).values_list('email', flat=True)
                list_email = [e for e in emails]
                print(list_email)
                [print(a.alimento_1_caducidad) for a in ali]
