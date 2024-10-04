from django.shortcuts import render
from .models import cpu
from .models import gpu
from.models import memory

# Create your views here.
def cpu_list(request):
    cpus = cpu.objects.all()
    return render(request, 'cpu_list.html', {"cpu_mostrar": cpus})

def gpu_list(request):
    gpus = gpu.objects.all()
    return render(request, 'gpu_list.html'  , {"gpu_mostrar" : gpus})

def memory_list(request):
    memorys = memory.objects.all()
    return render(request, 'memory_list.html' , {"memory_mostrar" : memorys})
