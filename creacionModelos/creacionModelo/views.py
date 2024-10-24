from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def lista_proyectos(request):
    proyectos = Proyecto.objects.select_related("creador").prefetch_related("usuarioAsignado")
    proyectos = proyectos.all()
    return render(request, 'proyecto/listar_proyectos.html', {"proyectos_mostrar" : proyectos})

def lista_tareas(request, proyecto_id):
    tareas = Tarea.objects.select_related("proyecto").filter(proyecto_id = proyecto_id)
    return render(request, 'tarea/listar_tareas.html', {"tareas_mostrar" : tareas})