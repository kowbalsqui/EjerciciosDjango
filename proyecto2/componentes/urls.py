from django.urls import path
from . import views

urlpatterns = [
    path("cpu", views.cpu_list, name='cpu_list'),
    path("gpu", views.gpu_list, name='gpu_list'),
    path("memory", views.memory_list, name='memory_list'),
]
