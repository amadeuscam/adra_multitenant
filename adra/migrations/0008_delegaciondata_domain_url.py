# Generated by Django 2.1.2 on 2021-02-23 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adra', '0007_delegaciondata_provincia'),
    ]

    operations = [
        migrations.AddField(
            model_name='delegaciondata',
            name='domain_url',
            field=models.CharField(default='', max_length=500),
        ),
    ]
