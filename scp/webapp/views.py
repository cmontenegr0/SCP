from django.shortcuts import render

# Create your views here.
from planeadores.models import Planeador


def adminSCP(request):
    no_planeadores = Planeador.objects.count()
    planeadores = Planeador.objects.order_by('id')
    dicc_planeadores = {'no_planeadores': no_planeadores,
                        'planeadores': planeadores}
    return render(request, 'admin_scp.html', dicc_planeadores)
