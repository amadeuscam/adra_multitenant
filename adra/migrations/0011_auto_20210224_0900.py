# Generated by Django 2.1.2 on 2021-02-24 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adra', '0010_gasto_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='importe',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]