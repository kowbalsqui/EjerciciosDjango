from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('Proyectos/listar', views.lista_proyectos, name= 'lista_proyectos'),
    path('Tareas/listar/<int:proyecto_id>', views.lista_tareas, name= 'lista_tareas'),
]
