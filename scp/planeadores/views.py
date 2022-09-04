from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from planeadores.forms import PlaneadorForm, FamiliaForm, EspecialidadForm, ClusterForm, UnidadForm, PlaneacionForm
from planeadores.models import Especialidad, Familia, Cluster, Unidad, Planeacion, Planeador


def planeador(request, id):
    planeador = get_object_or_404(Planeador, pk=id)
    # Aquí capturo todas las planeaciones que tiene el id recibido en los argumentos
    planeaciones = Planeacion.objects.filter(planeador=id)
    no_planxplan = Planeacion.objects.filter(planeador=id).count()
    dicc_planeador = {'planeador': planeador, 'planeaciones': planeaciones, 'no_planxplan': no_planxplan}

    return render(request, 'planeadores/planeador.html', dicc_planeador)

def agregarPlaneador(request):
    if request.method == 'POST':
        forma_planeador = PlaneadorForm(request.POST)
        if forma_planeador.is_valid():
            forma_planeador.save()
            return redirect('index')
    else:
        forma_planeador = PlaneadorForm()
    return render(request, 'planeadores/nuevo_planeador.html', {'forma_planeador': forma_planeador})

def home_especialidad(request):
    no_especialidades = Especialidad.objects.count()
    especialidades = Especialidad.objects.order_by('id')
    dicc_especialidades = {'no_especialidades': no_especialidades,
                        'especialidades': especialidades}
    return render(request, 'especialidades/home_especialidad.html', dicc_especialidades)

def agregarEspecialidad(request):
    if request.method == 'POST':
        forma_especialidad = EspecialidadForm(request.POST)
        if forma_especialidad.is_valid():
            forma_especialidad.save()
            return redirect('esp')
    else:
        forma_especialidad = EspecialidadForm()
    return render(request, 'especialidades/nueva_especialidad.html', {'forma_especialidad': forma_especialidad})

def home_familia(request):
    no_familias = Familia.objects.count()
    familias = Familia.objects.order_by('id')
    dicc_familias = {'no_familias': no_familias,
                        'familias': familias}
    return render(request, 'familias/home_familia.html', dicc_familias)

def agregarFamilia(request):
    if request.method == 'POST':
        forma_familia = FamiliaForm(request.POST)
        if forma_familia.is_valid():
            forma_familia.save()
            return redirect('fam')
    else:
        forma_familia = FamiliaForm()
    return render(request, 'familias/nueva_familia.html', {'forma_familia': forma_familia})

# Métodos del Cluster:
def cluster(request):
    no_clusters = Cluster.objects.count()
    clusters = Cluster.objects.order_by('sigla_cluster')
    dicc_clusters = {'no_clusters': no_clusters,
                     'clusters': clusters}
    return render(request, 'clusters/cluster.html', dicc_clusters)

def agregarCluster(request):
    if request.method == 'POST':
        forma_cluster = ClusterForm(request.POST)
        if forma_cluster.is_valid():
            forma_cluster.save()
            return redirect('clu')
    else:
        forma_cluster = ClusterForm()
    return render(request, 'clusters/nuevo_cluster.html', {'forma_cluster': forma_cluster})

# Métodos de la Unidad:
def unidad(request):
    no_unidades = Unidad.objects.count()
    unidades = Unidad.objects.order_by('numero_unidad')
    dicc_unidades = {'no_unidades': no_unidades,
                     'unidades': unidades}
    return render(request, 'unidades/unidad.html', dicc_unidades)

def agregarUnidad(request):
    if request.method == 'POST':
        forma_unidad = UnidadForm(request.POST)
        if forma_unidad.is_valid():
            forma_unidad.save()
            return redirect('und')
    else:
        forma_unidad = UnidadForm()
    return render(request, 'unidades/nueva_unidad.html', {'forma_unidad': forma_unidad})

def planeacion(request):
    no_planeaciones = Planeacion.objects.count()
    planeaciones = Planeacion.objects.order_by('id')
    dicc_planeaciones = {'no_planeaciones': no_planeaciones,
                     'planeaciones': planeaciones}
    return render(request, 'planeaciones/planeacion.html', dicc_planeaciones)

def agregarPlaneacion(request):
    if request.method == 'POST':
        forma_planeacion = PlaneacionForm(request.POST)
        if forma_planeacion.is_valid():
            forma_planeacion.save()
            return redirect('pla')
    else:
        forma_planeacion = PlaneacionForm()
    return render(request, 'planeaciones/nueva_planeacion.html', {'forma_planeacion': forma_planeacion})
