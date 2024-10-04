from django.shortcuts import render

# Create your views here.
def cpu_list(request):
    return render(request, 'cpu_list.html', {})

def gpu_list(request):
    return render(request, 'gpu_list.html'  , {})

def memory_list(request):
    return render(request, 'memory_list.html' , {})
