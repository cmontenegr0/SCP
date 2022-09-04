from django.contrib import admin

# Register your models here.
from planeadores.models import Planeador, Especialidad, Familia, Cluster, Unidad, Planeacion

admin.site.register(Planeador)
admin.site.register(Especialidad)
admin.site.register(Familia)
admin.site.register(Planeacion)
admin.site.register(Cluster)
admin.site.register(Unidad)
