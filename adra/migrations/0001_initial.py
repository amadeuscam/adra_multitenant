# Generated by Django 2.1.2 on 2021-02-21 08:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alimentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alimento_1', models.IntegerField(default=None, verbose_name='Arroz Blanco')),
                ('alimento_2', models.IntegerField(default=None, verbose_name='Alubia cocida')),
                ('alimento_3', models.IntegerField(default=None, verbose_name='Conserva de atún')),
                ('alimento_4', models.IntegerField(default=None, verbose_name='Conserva de sardina')),
                ('alimento_5', models.IntegerField(blank=True, default=None, null=True, verbose_name='Conserva de carne (magro de cerdo)')),
                ('alimento_6', models.IntegerField(default=None, verbose_name='Pasta alimenticia tipo macarrón')),
                ('alimento_7', models.IntegerField(default=None, verbose_name='Tomate frito en conserva')),
                ('alimento_8', models.IntegerField(default=None, verbose_name='Galletas')),
                ('alimento_9', models.IntegerField(default=None, verbose_name='Macedonia de verduras en conserva')),
                ('alimento_10', models.IntegerField(default=None, verbose_name='Fruta en conserva')),
                ('alimento_11', models.IntegerField(default=None, verbose_name='Tarritos infantiles con pollo')),
                ('alimento_12', models.IntegerField(default=None, verbose_name='Tarritos infantiles de fruta')),
                ('alimento_13', models.IntegerField(default=None, verbose_name='Leche entera UHT')),
                ('alimento_14', models.IntegerField(default=None, verbose_name='Batidos de chocolate')),
                ('alimento_15', models.IntegerField(default=None, verbose_name='Aceite de oliva')),
                ('fecha_recogida', models.DateTimeField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('modificado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Alimento',
                'verbose_name_plural': 'Alimentos',
                'ordering': ['-fecha_recogida'],
            },
        ),
        migrations.CreateModel(
            name='AlmacenAlimentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alimento_1', models.IntegerField(blank=True, null=True, verbose_name='Arroz Blanco')),
                ('alimento_2', models.IntegerField(blank=True, null=True, verbose_name='Alubia cocida')),
                ('alimento_3', models.IntegerField(blank=True, null=True, verbose_name='Conserva de atún')),
                ('alimento_4', models.IntegerField(blank=True, null=True, verbose_name='Conserva de sardina')),
                ('alimento_5', models.IntegerField(blank=True, null=True, verbose_name='Conserva de carne (magro de cerdo)')),
                ('alimento_6', models.IntegerField(blank=True, null=True, verbose_name='Pasta alimenticia tipo macarrón')),
                ('alimento_7', models.IntegerField(blank=True, null=True, verbose_name='Tomate frito en conserva')),
                ('alimento_8', models.IntegerField(blank=True, null=True, verbose_name='Galletas')),
                ('alimento_9', models.IntegerField(blank=True, null=True, verbose_name='Macedonia de verduras en conserva')),
                ('alimento_10', models.IntegerField(blank=True, null=True, verbose_name='Fruta en conserva')),
                ('alimento_11', models.IntegerField(blank=True, null=True, verbose_name='Tarritos infantiles con pollo')),
                ('alimento_12', models.IntegerField(blank=True, null=True, verbose_name='Tarritos infantiles de fruta')),
                ('alimento_13', models.IntegerField(blank=True, null=True, verbose_name='Leche entera UHT')),
                ('alimento_14', models.IntegerField(blank=True, null=True, verbose_name='Batidos de chocolate')),
                ('alimento_15', models.IntegerField(blank=True, null=True, verbose_name='Aceite de oliva')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('alimento_1_caducidad', models.DateField(blank=True, default=None, verbose_name='Arroz Blanco')),
                ('alimento_2_caducidad', models.DateField(blank=True, default=None, verbose_name='Alubia cocida')),
                ('alimento_3_caducidad', models.DateField(blank=True, default=None, verbose_name='Conserva de atún')),
                ('alimento_4_caducidad', models.DateField(blank=True, default=None, verbose_name='Conserva de sardina')),
                ('alimento_6_caducidad', models.DateField(blank=True, default=None, verbose_name='Pasta alimenticia tipo macarrón')),
                ('alimento_7_caducidad', models.DateField(blank=True, default=None, verbose_name='Tomate frito en conserva')),
                ('alimento_8_caducidad', models.DateField(blank=True, default=None, verbose_name='Galletas')),
                ('alimento_9_caducidad', models.DateField(blank=True, default=None, verbose_name='Macedonia de verduras en conserva')),
                ('alimento_10_caducidad', models.DateField(blank=True, default=None, verbose_name='Fruta en conserva')),
                ('alimento_11_caducidad', models.DateField(blank=True, default=None, verbose_name='Tarritos infantiles con pollo')),
                ('alimento_12_caducidad', models.DateField(blank=True, default=None, verbose_name='Tarritos infantiles de fruta')),
                ('alimento_13_caducidad', models.DateField(blank=True, default=None, verbose_name='Leche entera UHT')),
                ('alimento_14_caducidad', models.DateField(blank=True, default=None, verbose_name='Batidos de chocolate')),
                ('alimento_15_caducidad', models.DateField(blank=True, default=None, verbose_name='Aceite de oliva')),
                ('modificado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Almacen Alimento',
                'verbose_name_plural': 'Almacen Alimentos',
            },
        ),
        migrations.CreateModel(
            name='Hijo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentesco', models.CharField(choices=[('esposo', 'Esposo'), ('esposa', 'Esposa'), ('hijo', 'Hijo'), ('hija', 'Hija')], max_length=20)),
                ('sexo', models.CharField(choices=[('mujer', 'Mujer'), ('hombre', 'Hombre')], max_length=20)),
                ('nombre_apellido', models.CharField(max_length=50)),
                ('dni', models.CharField(blank=True, max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('edad', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True, verbose_name='Activo?')),
                ('modificado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Familiar del Beneficiario',
                'verbose_name_plural': 'Familiares del Beneficiario',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(max_length=100, verbose_name='Nombre del beneficiario')),
                ('dni', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('numero_adra', models.IntegerField(unique=True)),
                ('nacionalidad', models.CharField(max_length=20)),
                ('covid', models.BooleanField(default=False, verbose_name='Covid entregas')),
                ('domicilio', models.TextField()),
                ('are_acte', models.BooleanField(default=False, verbose_name='Tiene papeles')),
                ('ciudad', models.CharField(max_length=350)),
                ('telefono', models.IntegerField()),
                ('email', models.CharField(blank=True, default='', max_length=100, validators=[django.core.validators.EmailValidator()], verbose_name='Email beneficiario')),
                ('mensaje', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True, verbose_name='Activo?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('sexo', models.CharField(choices=[('mujer', 'Mujer'), ('hombre', 'Hombre')], max_length=20)),
                ('discapacidad', models.BooleanField(default=False)),
                ('domingo', models.CharField(choices=[('1', 'Domingo 1'), ('2', 'Domingo 2')], max_length=30)),
                ('empadronamiento', models.BooleanField(default=False, verbose_name='Certificado de empadronamiento actualizado con fecha de menos de tres meses ')),
                ('libro_familia', models.BooleanField(default=False, verbose_name='Fotocopia del Libro de Familia ')),
                ('fotocopia_dni', models.BooleanField(default=False, verbose_name='Fotocopia del DNI/NIE o pasaporte de todos los miembros del núcleo familiar')),
                ('prestaciones', models.BooleanField(default=False, verbose_name='Fotocopia de la documentación que acredite de prestación, pensión, paro, etc')),
                ('nomnia', models.BooleanField(default=False, verbose_name='Fotocopia de la nómina en caso de trabajar.')),
                ('cert_negativo', models.BooleanField(default=False, verbose_name='En caso de no tener ingresos: certificado negativo de rentas, de la Agencia Tributaria.')),
                ('aquiler_hipoteca', models.BooleanField(default=False, verbose_name='Ultimo recibo alquiler o  hipoteca de vivienda familiar en la que están empadronados')),
                ('recibos', models.BooleanField(default=False, verbose_name='Recibo de gastos básicos: luz, agua, gas, calefacción, comunidad y  comedor escolar.')),
                ('modificado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Beneficiario',
                'verbose_name_plural': 'Beneficiarios',
                'ordering': ('-created_at',),
            },
        ),
        migrations.AddField(
            model_name='hijo',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hijo', to='adra.Persona'),
        ),
        migrations.AddField(
            model_name='alimentos',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alimentos', to='adra.Persona'),
        ),
    ]
