from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('Proyectos/listar', views.lista_proyectos, name= 'lista_proyectos'),
    path('Tareas/listar/<int:proyecto_id>', views.lista_tareas, name= 'lista_tareas'),
    path('UsuarioTarea/listar/<int:tarea_id>', views.asignacionDeTarea, name= 'asignacionDeTarea'),
    path('Tareas/listarObservaciones/<str:texto>', views.tareaConObervacion, name= 'tareaConObervacion'),
    path('Tareas/listarEntreAñosyCompletadas/<int:año1>/<int:año2>', views.tareasCompletadaEntreAños, name = "tareasCompletadaEntreAños"),
    path('Usuario/listarUltimoUsuarioComento')
]
