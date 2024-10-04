from django.db import models
from django.conf import settings

# Create your models here.
class cpu(models.Model):
    vendedor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length= 100)
    precio = models.CharField(max_length=3)
    
    def __str__ (self):
        return self.nombre

class gpu(models.Model):
    nombre= models.CharField(max_length= 50)
    descripcion = models.CharField(max_length= 100)
    precio = models.CharField(max_length=3)
    
    def __str__ (self):
        return self.nombre
    
class memory(models.Model):
    nombre = models.CharField(max_length= 50)
    descripcion = models.CharField(max_length= 100)
    precio = models.CharField(max_length=3)
    
    def __str__ (self):
        return self.nombre