from django.db import models


activo = 'Activo'
finalizado = 'Finalizado'
SONDAJE_CHOICES = [(activo, 'Activo'), (finalizado, 'Finalizado'), ]

sup = 'Superficie'
int = 'Interior Mina'
OPERACIONES_CHOICES = [(sup, 'Superficie'), (int, 'Interior Mina'), ]

# Create your models here.
class Campagna(models.Model):
    id_campagna = models.AutoField(primary_key=True)
    nombre_campagna = models.CharField(verbose_name="Nombre Campaña", max_length=50)

    def __str__(self):
        return str(self.id_campagna) + " " + str(self.nombre_campagna)

    class Meta:
        db_table = 'campagnas'


class MotivosFinalizacione(models.Model):
    id_motivo = models.AutoField(primary_key=True)
    nombre_motivo = models.CharField(verbose_name="Nombre Motivo", max_length=50)
    descripcion_finalizacion = models.CharField(verbose_name="Estado Finalización", max_length=100)

    def __str__(self):
        return str(self.id_motivo) + " " + str(self.nombre_motivo)

    class Meta:
        db_table = 'motivo_finalizacion'


class Sondaje(models.Model):
    id_sondaje = models.AutoField(primary_key=True)
    nombre_sondaje = models.CharField(verbose_name="Nombre Sonsaje", max_length=50)
    macro_proyecto = models.CharField(verbose_name="Macroproyecto", max_length=50)
    sector = models.CharField(verbose_name="Sector", max_length=50)
    tipo_operacion = models.CharField(verbose_name="Tipo Operación", max_length=50, choices=OPERACIONES_CHOICES, default="Superficie")
    tipo_campagna = models.ForeignKey(Campagna, verbose_name="Tipo Campaña", on_delete=models.CASCADE)

    # categoria = models.CharField(verbose_name="Categoria", max_length=50)
    #  referencia ese campo"
    inclinacion = models.FloatField(verbose_name="Inclinación")
    azimuth = models.FloatField(verbose_name="Azimuth")
    profundidad_estimada = models.FloatField(verbose_name="Profundidad Estimada")
    estado_sondaje = models.CharField(verbose_name="Estado Sonsaje", choices=SONDAJE_CHOICES, default="activo", max_length=50)
    motivo_finalizacion = models.ForeignKey(MotivosFinalizacione, verbose_name="Motivo Finalización", max_length=100,
                                            on_delete=models.CASCADE, blank=True,null=True)
    def __str__(self):
        return str(self.nombre_sondaje)

    class Meta:
        db_table = 'sondajes'

class CodigosOperacione(models.Model):
    id_codigo = models.AutoField(primary_key=True)
    nombre_codigo= models.CharField(verbose_name="Nombre Código", max_length=50)

    def __str__(self):
        return str(self.nombre_codigo)

    class Meta:
        db_table = 'codigos_operacion'
