"""scp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from planeadores.views import agregarPlaneador, agregarEspecialidad, agregarFamilia, \
    home_especialidad, home_familia, cluster, unidad, agregarCluster, agregarUnidad, planeacion, agregarPlaneacion, \
    planeador
from webapp.views import adminSCP

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
    path('', adminSCP, name='index'),
    path('planeador/<int:id>', planeador, name='pl'),
    path('home_especialidad', home_especialidad, name='esp'),
    path('home_familia', home_familia, name='fam'),
    path('cluster', cluster, name='clu'),
    path('unidad', unidad, name='und'),
    path('planeacion', planeacion, name='pla'),
    path('nuevo_planeador', agregarPlaneador),
    path('nueva_planeacion', agregarPlaneacion),
    path('nueva_especialidad', agregarEspecialidad),
    path('nueva_familia', agregarFamilia),
    path('nuevo_cluster', agregarCluster),
    path('nueva_unidad', agregarUnidad),
]
