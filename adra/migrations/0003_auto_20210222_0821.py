# Generated by Django 2.1.2 on 2021-02-22 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adra', '0002_auto_20210222_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='otros_documentos',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
    ]
