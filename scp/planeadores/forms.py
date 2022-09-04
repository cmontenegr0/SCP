from django.forms import ModelForm, TextInput

from planeadores.models import Planeador, Especialidad, Familia, Planeacion, Cluster, Unidad


class PlaneadorForm(ModelForm):
    class Meta:
        model = Planeador
        fields = '__all__'
        #widgets = {

        #}

class EspecialidadForm(ModelForm):
    class Meta:
        model = Especialidad
        fields = '__all__'

class FamiliaForm(ModelForm):
    class Meta:
        model = Familia
        fields = '__all__'

class ClusterForm(ModelForm):
    class Meta:
        model = Cluster
        fields = '__all__'

class UnidadForm(ModelForm):
    class Meta:
        model = Unidad
        fields = '__all__'
        widgets = {
            'numero_unidad': TextInput(attrs={'type': 'number'})
        }

class PlaneacionForm(ModelForm):
    class Meta:
        model = Planeacion
        fields = '__all__'
        widgets = {
            'om': TextInput(attrs={'type': 'number'})
        }
