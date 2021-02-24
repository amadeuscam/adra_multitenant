import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adra_project.settings')
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from tenant_schemas_celery.app import CeleryApp as TenantAwareCeleryApp

# os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = TenantAwareCeleryApp()
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.timezone = 'Europe/Madrid'
# app.autodiscover_tasks()

#
# app = Celery('adra_project')
# app.config_from_object(settings, namespace='CELERY')
# app.autodiscover_tasks()
# app.conf.timezone = 'Europe/Madrid'
