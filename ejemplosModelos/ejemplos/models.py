from django.db import models

# Create your models here.
class Biblioteca (models.Model):
    nombre = models.CharField(max_length=100)
    codigoPostal = models.IntegerField(max_length=6)
    ciudad = models.CharField(max_length=100)
    
class Autor (models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200, blank= True)
    edad = models.IntegerField(null = True)

class Libro (models.Model):
    IDIOMAS = [
        ("ES", "Español"),
        ("EN", "Inglés"),
        ("FR", "Francés"),
        ("DE", "Alemán"),
    ]
    
    nombre = models.CharField(max_length= 100)
    tipo = models.CharField(
        max_length=2,
        choices=IDIOMAS,
        default="ES",
    )
    
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()
    biblioteca = models.ForeignKey(Biblioteca, on_delete = models.CASCADE)
    autores = models.ManyToManyField(Autor)
    
class Cliente (models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    puntos = models.FloatField(default=3)
    libros = models.ManyToManyField(Libro, through='Prestamos', related_name= "libross")
    libros_favoritos = models.ManyToManyField(Libro, through= 'Libros_Preferidos', related_name= "Favoritos")

class DatosClientes (models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    direccion = models.TextField()
    gustos = models.TextField()
    telefono = models.IntegerField()
    
class Prestamos (models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
class Libros_Preferidos (models.Model):
    libro = models.ForeignKey(Libro, on_delete= models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)