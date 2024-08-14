from django.contrib import admin
from .models import Campagna, MotivosFinalizacione, Sondaje, CodigosOperacione


# Personalizamos el admin de Campagna
class CampagnaAdmin(admin.ModelAdmin):
    list_display = ('id_campagna', 'nombre_campagna')
    search_fields = ('nombre_campagna',)
    list_filter = ('nombre_campagna',)
    ordering = ('nombre_campagna',)
    actions = ['make_inactive']

    def make_inactive(self, request, queryset):
        queryset.update(activo=False)

    make_inactive.short_description = "Marcar como inactivo"


# Personalizamos el admin de MotivosFinalizacione
class MotivosFinalizacioneAdmin(admin.ModelAdmin):
    list_display = ('id_motivo', 'nombre_motivo', 'descripcion_finalizacion')
    search_fields = ('nombre_motivo', 'descripcion_finalizacion')
    list_filter = ('nombre_motivo', 'descripcion_finalizacion')


# Personalizamos el admin de Sondaje
class SondajeAdmin(admin.ModelAdmin):
    list_display = (
        'id_sondaje', 'nombre_sondaje', 'macro_proyecto', 'sector', 'tipo_operacion', 'tipo_campagna', 'inclinacion',
        'azimuth', 'profundidad_estimada', 'estado_sondaje', 'motivo_finalizacion')
    search_fields = ('nombre_sondaje', 'macro_proyecto', 'sector', 'tipo_operacion', 'estado_sondaje')
    list_filter = ('macro_proyecto', 'sector', 'tipo_operacion', 'estado_sondaje', 'tipo_campagna')
    raw_id_fields = ('tipo_campagna', 'motivo_finalizacion')
    list_editable = ('estado_sondaje', 'inclinacion', 'azimuth', 'profundidad_estimada')
    prepopulated_fields = {"nombre_sondaje": ("macro_proyecto", "sector")}
    fieldsets = (
        (None, {
            'fields': ('nombre_sondaje', 'macro_proyecto', 'sector', 'tipo_operacion', 'tipo_campagna')
        }),
        ('Detalles', {
            'fields': ('inclinacion', 'azimuth', 'profundidad_estimada', 'estado_sondaje', 'motivo_finalizacion'),
        }),
    )


# Personalizamos el admin de CodigosOperacione
class CodigosOperacioneAdmin(admin.ModelAdmin):
    list_display = ('id_codigo', 'nombre_codigo')
    search_fields = ('nombre_codigo',)
    list_filter = ('nombre_codigo',)
    ordering = ('nombre_codigo',)


# Registramos los modelos personalizados en el admin
admin.site.register(Campagna, CampagnaAdmin)
admin.site.register(MotivosFinalizacione, MotivosFinalizacioneAdmin)
admin.site.register(Sondaje, SondajeAdmin)
admin.site.register(CodigosOperacione, CodigosOperacioneAdmin)
