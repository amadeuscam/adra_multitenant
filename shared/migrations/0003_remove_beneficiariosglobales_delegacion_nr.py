# Generated by Django 2.1.2 on 2021-03-03 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0002_beneficiariosglobales'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiariosglobales',
            name='delegacion_nr',
        ),
    ]