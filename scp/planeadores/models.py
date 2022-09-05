from django.db import models

# Create your models here.
class Unidad(models.Model):
    numero_unidad = models.CharField(max_length=255)
    nombre_unidad = models.CharField(max_length=255)

    def __str__(self):
        return f'Unidad {self.id} {self.numero_unidad} {self.nombre_unidad}'

class Cluster(models.Model):
    sigla_cluster = models.CharField(max_length=255)
    nombre_cluster = models.CharField(max_length=255)
    unidad = models.ForeignKey(Unidad, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Cluster {self.id} {self.sigla_cluster} {self.nombre_cluster} {self.unidad}'

class Familia(models.Model):
    nombre_familia = models.CharField(max_length=255)

    def __str__(self):
        return f'Familia {self.id} {self.nombre_familia}'

class Especialidad(models.Model):
    nombre_especialidad = models.CharField(max_length=255)

    def __str__(self):
        return f'Especialidad {self.id} {self.nombre_especialidad}'

class Planeador(models.Model):
    nombre_planeador = models.CharField(max_length=255)
    apellido_planeador = models.CharField(max_length=255)
    registro = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Planeador {self.id} {self.nombre_planeador} {self.apellido_planeador} {self.especialidad}'

class Planeacion(models.Model):
    om = models.IntegerField()
    tag_equipo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    fecha = models.DateField(auto_now=True)
    estado = models.CharField(max_length=255, editable=False, default='En planeación')
    planeador = models.ForeignKey(Planeador, on_delete=models.CASCADE)
    familia = models.ForeignKey(Familia, on_delete=models.SET_NULL, null=True)
    cluster = models.ForeignKey(Cluster, on_delete=models.SET_NULL, null=True)
    unidad = models.ForeignKey(Unidad, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Equipo {self.id} {self.cluster} {self.unidad} {self.familia} {self.tag_equipo} {self.om} ' \
               f'{self.descripcion} {self.estado} {self.planeador}'

class PlaneacionSAP(models.Model):
    om = models.IntegerField()
    tag_equipo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    fecha = models.DateField(auto_now=True)
    estado = models.CharField(max_length=255, default='En planeación', editable=False)
    planeador = models.ForeignKey(Planeador, on_delete=models.CASCADE)
    familia = models.ForeignKey(Familia, on_delete=models.SET_NULL, null=True)
    cluster = models.CharField(max_length=255)
    unidad = models.CharField(max_length=255)

    def __str__(self):
        return f'Equipo {self.id} {self.cluster} {self.unidad} {self.familia} {self.tag_equipo} {self.om} ' \
               f'{self.descripcion} {self.estado} {self.planeador}'
