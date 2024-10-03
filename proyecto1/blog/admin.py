from django.contrib import admin
from .models import Animal
from .models import Protectora
from .models import Colaborador

# Register your models here.

admin.site.register(Animal)
admin.site.register(Protectora)
admin.site.register(Colaborador)