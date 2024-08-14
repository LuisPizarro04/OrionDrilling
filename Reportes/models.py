from django.db import models
from Sondajes.models import CodigosOperacione, Sondaje

# Create your models here.
activo = 'Activo'
inactivo = 'Inactivo'
ESTADO_CHOICES = [(activo, 'Activo'), (inactivo, 'Inactivo'), ]

si = 'Si'
no = 'No'
pnd = 'Pendiente'
SI_NO_CHOICES = [(si, 'Si'), (no, 'No'), (pnd, 'Pendiente')]

a = 'A'
b = 'B'
TURNOS_CHOICES = [(a, 'A'), (b, 'B')]


class Maquinaria(models.Model):
    id_maquina = models.AutoField(primary_key=True)
    nombre_maquina = models.CharField(verbose_name="Nombre Maquina", max_length=50)
    estado_maquina = models.CharField(verbose_name="Estado Maquina", choices=ESTADO_CHOICES, default="activo",
                                      max_length=50)

    def __str__(self):
        return str(self.nombre_maquina)

    class Meta:
        db_table = 'maquinas'


class Operadore(models.Model):
    id_operador = models.AutoField(primary_key=True)
    nombre_operador = models.CharField(verbose_name="Nombre operador", max_length=50)
    estado_operador = models.CharField(verbose_name="Estado operador", choices=ESTADO_CHOICES, default="activo",
                                       max_length=50)

    def __str__(self):
        return str(self.nombre_operador)

    class Meta:
        db_table = 'operadores'


class Ayudantes(models.Model):
    id_ayudante = models.AutoField(primary_key=True)
    nombre_ayudante = models.CharField(verbose_name="Nombre Ayudante", max_length=50)
    estado_ayudante = models.CharField(verbose_name="Estado Ayudante", choices=ESTADO_CHOICES, default="activo",
                                       max_length=50)

    def __str__(self):
        return str(self.nombre_ayudante)

    class Meta:
        db_table = 'ayudantes'


class Perforacione(models.Model):
    id_perforacion = models.AutoField(primary_key=True)
    desde = models.TimeField(verbose_name="Inicio actividad")
    hasta = models.TimeField(verbose_name="Final actividad")
    metros_perforados = models.FloatField(verbose_name="Metros Perforados")
    porcentaje_recuperacion = models.FloatField(verbose_name="Metros Perforados")

    """def __str__(self):
            return str(self.nombre_ayudante)"""

    class Meta:
        db_table = 'perforaciones'


class Reporte(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    id_sondaje = models.ForeignKey(Sondaje, on_delete=models.CASCADE, max_length=50)
    fecha = models.DateField(verbose_name="Fecha Reporte")
    turno = models.CharField(verbose_name="Turno reporte", choices=TURNOS_CHOICES, default="A", max_length=2)
    desde = models.TimeField(verbose_name="Desde")
    hasta = models.TimeField(verbose_name="Hasta")
    hrs_trabajadas = models.TimeField(verbose_name="Horas trabajadas")
    id_equipo = models.ForeignKey(Maquinaria, on_delete=models.CASCADE, max_length=50)
    id_operador = models.ForeignKey(Operadore, on_delete=models.CASCADE, max_length=50)
    id_ayudante_1 = models.ForeignKey(Ayudantes, on_delete=models.CASCADE, max_length=50)
    profundidad_inicial = models.FloatField(verbose_name="Profundidad Inicial")
    profundidad_final = models.FloatField(verbose_name="Profundidad Final")
    perforado = models.FloatField(verbose_name="Profundidad Final")
    horometro_inicial = models.TimeField(verbose_name="Horometro Inicial")
    horometro_final = models.TimeField(verbose_name="Horometro Final")



    # id_ayudante_2 = models.ForeignKey(Ayudantes, on_delete=models.CASCADE, max_length=50)

    def __str__(self):
        return str(self.id_reporte) + "-" + str(self.id_equipo) + "-" + str(self.id_operador)

    class Meta:
        db_table = 'reportes'


class Actividades(models.Model):
    id_actividad = models.AutoField(primary_key=True)
    id_reporte = models.ForeignKey(Reporte, on_delete=models.CASCADE, max_length=50)
    id_cod_operacion = models.ForeignKey(CodigosOperacione, on_delete=models.CASCADE, max_length=50)
    desde = models.TimeField(verbose_name="Inicio actividad")
    hasta = models.TimeField(verbose_name="Final actividad")
    total = models.IntegerField()
    cargo_hora_contratista = models.CharField(verbose_name="Cargo a Cont", choices=SI_NO_CHOICES, default="Pendiente",
                                              max_length=50)
    cargo_hora_cliente = models.CharField(verbose_name="Cargo Cliente", choices=SI_NO_CHOICES, default="Pendiente",
                                          max_length=50)

    """def __str__(self):
        return str(self.nombre_ayudante)"""

    class Meta:
        db_table = 'actividades'
