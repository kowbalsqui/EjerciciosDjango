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
    tareas = Tarea.objects.select_related("proyecto").filter(proyecto_id = proyecto_id).order_by("-fechaCreacion")
    return render(request, 'tarea/listar_tareas.html', {"tareas_mostrar" : tareas})

def asignacionDeTarea (request, tarea_id):
    usuario = Usuario.objects.filter(usuarios_tareas__tarea=tarea_id).order_by()
    return render(request, 'usuario/listarusuariosConTarea.html', {"usuarioTarea_mostrar": usuario})  

def tareaConObervacion (request, texto):
    tarea = Tarea.objects.filter(asignaciondetarea__observaciones__contains = texto)
    return render(request, 'tarea/listar_tareas_observaciones.html', {"tareas_mostrar" : tarea})

def tareasCompletadaEntreAños(request, año1, año2):
    tareas = Tarea.objects.filter(fechaCreacion__year__gte=año1,fechaCreacion__year__lte=año2, estado = 'Completada').all()
    return render(request, 'tarea/listar_tareas_completadas_entre_años.html', {"tareas_mostrar" : tareas})

