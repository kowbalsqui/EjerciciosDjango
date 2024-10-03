from django.shortcuts import render
from .models import Animal
from .models import Protectora
from .models import Colaborador

# Create your views here.

def animal_list (request):
    animales = Animal.objects.all()
    return render(request, 'blog/animal_list.html', {"animales_mostrar":animales})

def protectora_list (request):
    protectoras = Protectora.objects.all()
    return render(request, 'blog/protectora_list.html', {"protectoras_mostrar":protectoras})

def colaborador_list(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'blog/colaborador_list.html', {"colaboradores_mostrar":colaboradores})