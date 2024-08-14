from django.contrib import admin
from .models import Maquinaria, Operadore, Ayudantes, Perforacione, Reporte, Actividades


# Personalizamos el admin de Maquinaria
class MaquinariaAdmin(admin.ModelAdmin):
    list_display = ('id_maquina', 'nombre_maquina', 'estado_maquina')
    search_fields = ('nombre_maquina',)
    list_filter = ('estado_maquina',)
    ordering = ('nombre_maquina',)


# Personalizamos el admin de Operadore
class OperadoreAdmin(admin.ModelAdmin):
    list_display = ('id_operador', 'nombre_operador', 'estado_operador')
    search_fields = ('nombre_operador',)
    list_filter = ('estado_operador',)
    ordering = ('nombre_operador',)


# Personalizamos el admin de Ayudantes
class AyudantesAdmin(admin.ModelAdmin):
    list_display = ('id_ayudante', 'nombre_ayudante', 'estado_ayudante')
    search_fields = ('nombre_ayudante',)
    list_filter = ('estado_ayudante',)
    ordering = ('nombre_ayudante',)


# Personalizamos el admin de Perforacione
class PerforacioneAdmin(admin.ModelAdmin):
    list_display = ('id_perforacion', 'desde', 'hasta', 'metros_perforados', 'porcentaje_recuperacion')
    search_fields = ('id_perforacion',)
    list_filter = ('metros_perforados', 'porcentaje_recuperacion')
    ordering = ('id_perforacion',)


# Inline para Actividades
class ActividadesInline(admin.TabularInline):
    model = Actividades
    extra = 1


# Personalizamos el admin de Reporte
class ReporteAdmin(admin.ModelAdmin):
    list_display = (
        'id_reporte', 'id_sondaje', 'fecha', 'turno', 'desde', 'hasta', 'hrs_trabajadas', 'id_equipo', 'id_operador',
        'id_ayudante_1', 'profundidad_inicial', 'profundidad_final', 'perforado', 'horometro_inicial',
        'horometro_final')
    search_fields = ('id_reporte', 'id_sondaje', 'id_equipo', 'id_operador', 'id_ayudante_1')
    list_filter = ('id_sondaje', 'id_equipo', 'id_operador', 'fecha', 'turno')
    ordering = ('id_reporte',)
    inlines = [ActividadesInline]  # Añadir el inline aquí


# Personalizamos el admin de Actividades
class ActividadesAdmin(admin.ModelAdmin):
    list_display = (
        'id_actividad', 'id_reporte', 'id_cod_operacion', 'desde', 'hasta', 'total', 'cargo_hora_contratista',
        'cargo_hora_cliente')
    search_fields = ('id_actividad', 'id_reporte', 'id_cod_operacion')
    list_filter = ('cargo_hora_contratista', 'cargo_hora_cliente')
    ordering = ('id_actividad',)


# Registramos los modelos personalizados en el admin
admin.site.register(Maquinaria, MaquinariaAdmin)
admin.site.register(Operadore, OperadoreAdmin)
admin.site.register(Ayudantes, AyudantesAdmin)
admin.site.register(Perforacione, PerforacioneAdmin)
admin.site.register(Reporte, ReporteAdmin)
admin.site.register(Actividades, ActividadesAdmin)
