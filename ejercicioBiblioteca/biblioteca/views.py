from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.db.models import Avg, Max, Min

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listar_libros (request):
    libro = Libro.objects.select_related('biblioteca').prefetch_related('autores')
    libro = libro.all()
    return render(request, 'lista.html', {'libro_mostrar': libro})

def dame_libro(request, id_libro):
    QSlibro = Libro.objects.select_related('biblioteca').prefetch_related('autores')
    libro = QSlibro.get(id=id_libro)  # En caso de que el libro no exista, el método get() lanzará un ObjectDoesNotExist.
    return render(request, 'libro.html', {'libro_mostrar': libro})

def dame_libro_fecha(request, anyo_libro, mes_libro):
    QSlibro = Libro.objects.select_related('biblioteca').prefetch_related('autores')
    libros = QSlibro.filter(fecha_publicacion__year=anyo_libro, fecha_publicacion__month=mes_libro)
    return render(request, 'lista.html', {'libro_mostrar': libros})

def dame_libros_idioma (request, tipo):
    QSlibro = Libro.objects.select_related('biblioteca').prefetch_related("autores")
    libros = QSlibro.filter(Q(tipo = tipo) | Q(tipo= "ES")).order_by("fecha_publicacion")
    return render(request, "lista.html", {"libro_mostrar" : libros})

def dame_libros_biblioteca (request, id_biblioteca, texto_libro):
    QSlibro = Libro.objects.select_related('biblioteca').prefetch_related('autores')
    libros = QSlibro.filter(biblioteca=id_biblioteca).filter(descripcion__contains= texto_libro).order_by("-nombre")
    return render(request, "lista.html", {"libro_mostrar": libros})

def dame_ultimo_cliente_libro(request, libro):
    cliente = Cliente.objects.filter(prestamo__libro = libro).order_by("-prestamo__fecha_prestamo")[:1].get()
    return render(request, "cliente.html", {"cliente": cliente})

def dame_agrupaciones_puntos_cliente(request):
    resultado = Cliente.objects.aggregate(Avg("puntos"), Max("puntos"), Min("puntos"))
    media = resultado ["untos__avg"]
    maximo = resultado["puntos__max"]
    minimo = resultado["puntos__min"]
    return render (request, "agrupaciones.html",{"media": media, "maximo": maximo, "minimo": minimo})