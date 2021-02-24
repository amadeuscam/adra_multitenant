from datetime import datetime
import sendgrid
from celery.decorators import periodic_task

from celery.schedules import crontab
from django.contrib.auth.models import User
from .models import AlmacenAlimentos, Persona
from django.conf import settings
import subprocess
from pathlib import Path
import shutil
import time
import shlex
import glob, os
import pathlib

import zipfile
from io import BytesIO;
from celery import shared_task
from mailmerge import MailMerge
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
from django.db import connection
from adra_project.celery import app
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.sites.models import Site
# from celery_app import app
# from django_tenants.utils import get_tenant_model, tenant_context
from tenant_schemas.utils import get_tenant_model, tenant_context
from django.db import connection

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'check_caducidad_todas_delegaciones',
        # 'schedule': crontab(minute=30, hour='7'),
        'schedule': crontab(),
    },
    'restart_telefram': {
        'task': 'restart_telefram_bot',
        # 'schedule': crontab(minute=0, hour='6,18'),
        'schedule': crontab(),
    },
    'database_backup': {
        'task': 'make_backup_database',
        # 'schedule': crontab(minute=0, hour='6,18'),
        'schedule': crontab(),
    },
}


def caduca(fecha):
    date_format = "%Y-%m-%d"
    a = datetime.strptime(str(datetime.now().date()), date_format)
    b = datetime.strptime(str(fecha), date_format)
    delta_aceite = b - a
    return delta_aceite.days


@app.task(name='check_caducidad_todas_delegaciones')
def check_caducidad_todas_delegaciones():
    for tenant in get_tenant_model().objects.exclude(schema_name='public', code=0):
        connection.set_tenant(tenant)
        sg = sendgrid.SendGridAPIClient(settings.SENDGRID_API_KEY)
        ali = AlmacenAlimentos.objects.all()
        emails = User.objects.filter(is_active=True, is_staff=True).values_list('email', flat=True)
        list_email = [e for e in emails]

        for al in ali:
            # print(caduca(al.alimento_1_caducidad))

            if caduca(al.alimento_1_caducidad) == 37:
                alimento_1_name = al._meta.get_field('alimento_1').verbose_name

                print(tenant)
                print(list_email)
                print(alimento_1_name)
                print('-' * 90)

                # message = sendgrid.Mail(
                #     from_email=f"admin@adra.es",
                #     to_emails=list_email,
                # )
                # message.dynamic_template_data = {
                #     "alimento": f"{alimento_1_name}",
                #     "delegacion": f"{tenant}",
                #     "Sender_Name": f"{tenant}",
                #     "Sender_Address": f"calle primavera 15",
                #     "Sender_City": f"Torrejon de ardoz",
                #     "Sender_State": f"Madrid",
                #     "Sender_Zip": f"28850"
                # }
                # message.template_id = 'd-b3a251b22c7442b39b79ddc901020457'
                # res = sg.send(message)
                # print(message)

            if caduca(al.alimento_2_caducidad) == 0:
                alimento_2_name = AlmacenAlimentos._meta.get_field('alimento_2').verbose_name

                print(tenant)
                print(list_email)
                print(alimento_2_name)
                print('-' * 90)
                # message = sendgrid.Mail(
                #     from_email=f"admin@adra.es",
                #     to_emails=list_email,
                # )
                # message.dynamic_template_data = {
                #     "alimento": f"{alimento_2_name}",
                #     "delegacion": f"{tenant}",
                #     "Sender_Name": f"{tenant}",
                #     "Sender_City": f"Torrejon de ardoz",
                #     "Sender_State": f"Madrid",
                #     "Sender_Zip": f"28850"
                # }
                # message.template_id = 'd-b3a251b22c7442b39b79ddc901020457'
                # res = sg.send(message)
                # print(res.status_code)

            if caduca(al.alimento_3_caducidad) == 37:
                alimento_3_name = AlmacenAlimentos._meta.get_field('alimento_3').verbose_name
                message = sendgrid.Mail(
                    from_email=f"admin@adra.es",
                    to_emails=list_email,
                )
                message.dynamic_template_data = {
                    "alimento": f"{alimento_3_name}",
                    "Sender_Name": f"Adra Torrejon de ardoz",
                    "Sender_Address": f"calle primavera 15",
                    "Sender_City": f"Torrejon de ardoz",
                    "Sender_State": f"Madrid",
                    "Sender_Zip": f"28850"
                }
                message.template_id = 'd-b3a251b22c7442b39b79ddc901020457'
                res = sg.send(message)
                print(res.status_code)

            if caduca(al.alimento_4_caducidad) == 37:
                alimento_4_name = AlmacenAlimentos._meta.get_field('alimento_4').verbose_name
                message = sendgrid.Mail(
                    from_email=f"admin@adra.es",
                    to_emails=list_email,
                )
                message.dynamic_template_data = {
                    "alimento": f"{alimento_4_name}",
                    "Sender_Name": f"Adra Torrejon de ardoz",
                    "Sender_Address": f"calle primavera 15",
                    "Sender_City": f"Torrejon de ardoz",
                    "Sender_State": f"Madrid",
                    "Sender_Zip": f"28850"
                }
                message.template_id = 'd-b3a251b22c7442b39b79ddc901020457'
                res = sg.send(message)
                print(res.status_code)

            if caduca(al.alimento_6_caducidad) == 37:
                alimento_6_name = AlmacenAlimentos._meta.get_field('alimento_6').verbose_name
                message = sendgrid.Mail(
                    from_email=f"admin@adra.es",
                    to_emails=list_email,
                )
                message.dynamic_template_data = {
                    "alimento": f"{alimento_6_name}",
                    "Sender_Name": f"Adra Torrejon de ardoz",
                    "Sender_Address": f"calle primavera 15",
                    "Sender_City": f"Torrejon de ardoz",
                    "Sender_State": f"Madrid",
                    "Sender_Zip": f"28850"
                }
                message.template_id = 'd-b3a251b22c7442b39b79ddc901020457'
                res = sg.send(message)
                print(res.status_code)

            if caduca(al.alimento_7_caducidad) == 37:
                alimento_7_name = AlmacenAlimentos._meta.get_field('alimento_7').verbose_name
                message = sendgrid.Mail(
                    from_email=f"admin@adra.es",
                    to_emails=list_email,
                )
                message.dynamic_template_data = {
                    "alimento": f"{alimento_7_name}",
                    "Sender_Name": f"Adra Torrejon de ardoz",
                    "Sender_Address": f"calle primavera 15",
                    "Sender_City": f"Torrejon de ardoz",
                    "Sender_State": f"Madrid",
                    "Sender_Zip": f"28850"
                }
                message.template_id = 'd-b3a251b22c7442b39b79ddc901020457'
                res = sg.send(message)
                print(res.status_code)

            if caduca(al.alimento_8_caducidad) == 37:
                alimento_8_name = AlmacenAlimentos._meta.get_field('alimento_8').verbose_name
                message = sendgrid.Mail(
                    from_email=f"admin@adra.es",
                    to_emails=list_email,
                )
                message.dynamic_template_data = {
                    "alimento": f"{alimento_8_name}",
                    "Sender_Name": f"Adra Torrejon de ardoz",
                    "Sender_Address": f"calle primavera 15",
                    "Sender_City": f"Torrejon de ardoz",
                    "Sender_State": f"Madrid",
                    "Sender_Zip": f"28850"
                }
                message.template_id = 'd-b3a251b22c7442b39b79ddc901020457'
                res = sg.send(message)
                print(res.status_code)

            if caduca(al.alimento_9_caducidad) == 37:
                alimento_9_name = AlmacenAlimentos._meta.get_field('alimento_9').verbose_name
                message = sendgrid.Mail(
                    from_email=f"admin@adra.es",
                    to_emails=list_email,
                )
                message.dynamic_template_data = {
                    "alimento": f"{alimento_9_name}",
                    "Sender_Name": f"Adra Torrejon de ardoz",
                    "Sender_Address": f"calle primavera 15",
                    "Sender_City": f"Torrejon de ardoz",
                    "Sender_State": f"Madrid",
                    "Sender_Zip": f"28850"
                }
                message.template_id = 'd-b3a251b22c7442b39b79ddc901020457'
                res = sg.send(message)
                print(res.status_code)

            if caduca(al.alimento_10_caducidad) == 37:
                alimento_10_name = AlmacenAlimentos._meta.get_field('alimento_10').verbose_name
                message = sendgrid.Mail(
                    from_email=f"admin@adra.es",
                    to_emails=list_email,
                )
                message.dynamic_template_data = {
                    "alimento": f"{alimento_10_name}",
                    "Sender_Name": f"Adra Torrejon de ardoz",
                    "Sender_Address": f"calle primavera 15",
                    "Sender_City": f"Torrejon de ardoz",
                    "Sender_State": f"Madrid",
                    "Sender_Zip": f"28850"
                }
                message.template_id = 'd-b3a251b22c7442b39b79ddc901020457'
                res = sg.send(message)
                print(res.status_code)

            if caduca(al.alimento_11_caducidad) == 37:
                alimento_11_name = AlmacenAlimentos._meta.get_field('alimento_11').verbose_name
                message = sendgrid.Mail(
                    from_email=f"admin@adra.es",
                    to_emails=list_email,
                )
                message.dynamic_template_data = {
                    "alimento": f"{alimento_11_name}",
                    "Sender_Name": f"Adra Torrejon de ardoz",
                    "Sender_Address": f"calle primavera 15",
                    "Sender_City": f"Torrejon de ardoz",
                    "Sender_State": f"Madrid",
                    "Sender_Zip": f"28850"
                }
                message.template_id = 'd-b3a251b22c7442b39b79ddc901020457'
                res = sg.send(message)
                print(res.status_code)

            if caduca(al.alimento_12_caducidad) == 37:
                alimento_12_name = AlmacenAlimentos._meta.get_field('alimento_12').verbose_name
                message = sendgrid.Mail(
                    from_email=f"admin@adra.es",
                    to_emails=list_email,
                )
                message.dynamic_template_data = {
                    "alimento": f"{alimento_12_name}",
                    "Sender_Name": f"Adra Torrejon de ardoz",
                    "Sender_Address": f"calle primavera 15",
                    "Sender_City": f"Torrejon de ardoz",
                    "Sender_State": f"Madrid",
                    "Sender_Zip": f"28850"
                }
                message.template_id = 'd-b3a251b22c7442b39b79ddc901020457'
                res = sg.send(message)
                print(res.status_code)

            if caduca(al.alimento_13_caducidad) == 37:
                alimento_13_name = AlmacenAlimentos._meta.get_field('alimento_13').verbose_name
                message = sendgrid.Mail(
                    from_email=f"admin@adra.es",
                    to_emails=list_email,
                )
                message.dynamic_template_data = {
                    "alimento": f"{alimento_13_name}",
                    "Sender_Name": f"Adra Torrejon de ardoz",
                    "Sender_Address": f"calle primavera 15",
                    "Sender_City": f"Torrejon de ardoz",
                    "Sender_State": f"Madrid",
                    "Sender_Zip": f"28850"
                }
                message.template_id = 'd-b3a251b22c7442b39b79ddc901020457'
                res = sg.send(message)
                print(res.status_code)

            if caduca(al.alimento_14_caducidad) == 37:
                alimento_14_name = AlmacenAlimentos._meta.get_field('alimento_14').verbose_name
                message = sendgrid.Mail(
                    from_email=f"admin@adra.es",
                    to_emails=list_email,
                )
                message.dynamic_template_data = {
                    "alimento": f"{alimento_14_name}",
                    "Sender_Name": f"Adra Torrejon de ardoz",
                    "Sender_Address": f"calle primavera 15",
                    "Sender_City": f"Torrejon de ardoz",
                    "Sender_State": f"Madrid",
                    "Sender_Zip": f"28850"
                }
                message.template_id = 'd-b3a251b22c7442b39b79ddc901020457'
                res = sg.send(message)
                print(res.status_code)

            if caduca(al.alimento_15_caducidad) == 37:
                alimento_15_name = AlmacenAlimentos._meta.get_field('alimento_15').verbose_name
                message = sendgrid.Mail(
                    from_email=f"admin@adra.es",
                    to_emails=list_email,
                )
                message.dynamic_template_data = {
                    "alimento": f"{alimento_15_name}",
                    "Sender_Name": f"Adra Torrejon de ardoz",
                    "Sender_Address": f"calle primavera 15",
                    "Sender_City": f"Torrejon de ardoz",
                    "Sender_State": f"Madrid",
                    "Sender_Zip": f"28850"
                }
                message.template_id = 'd-b3a251b22c7442b39b79ddc901020457'
                res = sg.send(message)
                print(res.status_code)


@app.task(name='restart_telefram_bot')
def restart_telefram_bot():
    print("telegram bot.............")
    # subprocess.call(["supervisorctl", "restart", "telegram"])


@app.task(name='make_backup_database')
def make_backup_mysql():
    print("database backup.............")
    # username = settings.USER_DB
    # password = settings.PASSWORD_DB
    # database = settings.NAME_DB
    #
    # command_line = f"mysqldump -u {username} -p{password}  {database} > {datetime.now().day}-{datetime.now().month}.sql"
    # # os.popen(command_line)
    #
    # dc = subprocess.Popen(command_line, shell=True)
    # dc.wait()


# @shared_task(name='delete_folder')
# def delete_folder():
#     print("borrar la carpeta de los zip")
#     shutil.rmtree('./valoracion',ignore_errors=True)
#
#
# @shared_task(name='export_zip')
# def export_zip(fecha):
#     persona = Persona.objects.filter(active=True).exclude(covid=True).order_by("numero_adra")
#
#     dirN = "./valoracion"
#
#     if not os.path.exists(dirN):
#         os.makedirs(dirN)
#         print("Directory ", dirN, " created")
#     else:
#         print("Directory ", dirN, " exists")
#
#     template = "./vl.docx"
#     for p in persona:
#         print(p.nombre_apellido)
#         hijos = []
#         document = MailMerge(template)
#         for h in p.hijo.all():
#             hijo_dict = {}
#             hijo_dict['parentesco'] = f'{h.parentesco}'
#             hijo_dict['nombre_apellido_hijo'] = f'{h.nombre_apellido}'
#             hijo_dict['dni_hijo'] = f'{h.dni}'
#             hijo_dict['pas_hijo'] = f'{h.otros_documentos}'
#             hijo_dict['fecha_nacimiento_hijo'] = f"{'{:%d-%m-%Y}'.format(h.fecha_nacimiento)}"
#             hijos.append(hijo_dict)
#         document.merge(
#             numar_adra=f'{p.numero_adra}',
#             nombre_apellido=f'{p.nombre_apellido}',
#             dni=f'{p.dni}',
#             fecha_nacimiento=f"{'{:%d-%m-%Y}'.format(p.fecha_nacimiento)}",
#             nacionalidad=f'{p.nacionalidad}',
#             domicilio=f'{p.domicilio}',
#             ciudad=f'{p.ciudad}',
#             numar_telefon=f'{p.telefono}',
#             # fecha_hoy=f"{'{:%d-%m-%Y}'.format(date.today())}",
#             fecha_hoy=f"{fecha}",
#
#         )
#         if p.empadronamiento:
#             document.merge(a="x")
#         if p.libro_familia:
#             document.merge(b="x")
#         if p.fotocopia_dni:
#             document.merge(c="x")
#         if p.prestaciones:
#             document.merge(d="x")
#         if p.nomnia:
#             document.merge(e="x")
#         if p.cert_negativo:
#             document.merge(f="x")
#         if p.aquiler_hipoteca:
#             document.merge(g="x")
#         if p.recibos:
#             document.merge(h="x")
#         document.merge_rows('parentesco', hijos)
#         document.write(f'./valoracion/{p.numero_adra}.docx')
#
#     filenames = []
#     os.chdir("./valoracion")
#     for file in glob.glob("*.docx"):
#         filenames.append(str(file))
#
#     zip_subdir = f"valoracion_social"
#     zip_filename = "%s.zip" % zip_subdir
#
#     # Open StringIO to grab in-memory ZIP contents
#     zip_io = BytesIO()
#     # response = HttpResponse(content_type='application/zip')
#     # The zip compressor
#     print(filenames)
#     with zipfile.ZipFile(zip_io, mode='w', compression=zipfile.ZIP_BZIP2) as backup_zip:
#
#         for file in filenames:
#             # Calculate path for file in zip
#             fdir, fname = os.path.split(file)
#             zip_path = os.path.join(zip_subdir, fname)
#             # # Add file, at correct path
#             backup_zip.write(file, zip_path)
#
#     response = HttpResponse(zip_io.getvalue(), content_type="application/octet-stream")
#     response['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
#     return response
