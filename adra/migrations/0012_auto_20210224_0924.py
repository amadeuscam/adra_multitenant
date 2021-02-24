# Generated by Django 2.1.2 on 2021-02-24 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adra', '0011_auto_20210224_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='gasto',
            name='tipo',
            field=models.CharField(choices=[('ingreso', 'Ingreso'), ('gasto', 'Gasto')], default='', max_length=50),
        ),
    ]