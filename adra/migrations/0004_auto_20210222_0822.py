# Generated by Django 2.1.2 on 2021-02-22 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adra', '0003_auto_20210222_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='dni',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
