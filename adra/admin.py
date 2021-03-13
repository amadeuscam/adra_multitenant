from django.contrib import admin
from django.conf import settings

from .models import Persona, Alimentos, AlmacenAlimentos, Hijo, DelegacionData,Gasto


# Register your models here.

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['user', 'date_of_birth']




class HijoInline(admin.TabularInline):
    model = Hijo


@admin.register(Hijo)
class HijoAdmin(admin.ModelAdmin):
    search_fields = ("nombre_apellido",)
    list_display = ("nombre_apellido", "persona", "modificado_por",)
    list_per_page = 15


class PersonaAdmin(admin.ModelAdmin):
    inlines = [HijoInline]
    list_filter = ("domingo", 'covid',)
    search_fields = ("nombre_apellido", "numero_adra",)
    list_display = ("nombre_apellido", "numero_adra", "mensaje", 'covid',)
    list_display_links = ("numero_adra", "nombre_apellido",)
    list_editable = ("covid",)
    list_per_page = 15
    sortable_by = ("numero_adra",)
    ordering = ('nombre_apellido', 'numero_adra')


class AlimentosAdmin(admin.ModelAdmin):
    list_display = ("fecha_recogida", "persona",)
    list_per_page = 15


class DelegacionesAdmin(admin.ModelAdmin):
    # readonly_fields = ('domain_url',)
    pass

admin.site.register(Persona, PersonaAdmin)
# admin.site.register(Hijo)
admin.site.register(Alimentos, AlimentosAdmin)
admin.site.register(AlmacenAlimentos)
admin.site.register(Gasto)
admin.site.register(DelegacionData, DelegacionesAdmin)
# custom names admin site
# admin.site.index_title = request.session.platform_name

# if dele:
#     admin.site.site_header = f"Administración {dele.nombre} "
#     admin.site.site_title = "Adra"
