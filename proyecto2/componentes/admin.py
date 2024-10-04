from django.contrib import admin
from .models import gpu
from .models import memory
from .models import cpu
# Register your models here.
admin.site.register(cpu)
admin.site.register(gpu)
admin.site.register(memory)