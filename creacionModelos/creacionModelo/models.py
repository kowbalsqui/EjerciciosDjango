from django.db import models

# Modelo de Usuario
class Usuario(models.Model):
    nombre = models.TextField(max_length=100)
    correoElectronico = primay_key = True, models.TextField(max_length= 100)  # Definir correctamente la clave primaria
    contraseña = models.TextField(max_length=100)  # "contraseña" corregido
    fechaRegistro = models.DateField()

# Modelo de Tarea
class Tarea(models.Model):
    titulo = models.TextField(max_length=100)
    descripcion = models.TextField(max_length=200)
    prioridad = models.IntegerField()
    
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('En progreso', 'En progreso'),
        ('Completada', 'Completada'),
    ]
    
    estado = models.TextField(choices=ESTADOS, default='Pendiente')
    completada = models.BooleanField(default=False)
    fechaCreacion = models.DateField()
    horaVencimiento = models.DateTimeField()
    
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tareas_creadas')  # related_name para evitar conflictos
    usuariosAsignados = models.ManyToManyField(Usuario, through='Usuarios_Tareas', related_name='tareas_asignadas')

# Modelo de Proyecto
class Proyecto(models.Model):
    nombre = models.TextField(max_length=100)
    descripcion = models.TextField(max_length=200)
    duracionEstimada = models.FloatField()
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    
    usuarioAsignado = models.ManyToManyField(Usuario, through='Usuario_Proyecto', related_name='proyectos_asignados')
    creador = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='proyectos_creados')
    
    tareas = models.ForeignKey(Tarea, on_delete=models.CASCADE)  # Cambiado a ManyToMany para reflejar que un proyecto tiene varias tareas

# Modelo de Etiqueta
class Etiqueta(models.Model):
    nombre = primay_key = True, models.TextField(max_length= 100)  # Definir correctamente la clave primaria
    etiquetasDeTareas = models.ManyToManyField(Tarea, through='Tarea_Etiqueta')

# Modelo de Asignación de Tarea (Podría usarse para hacer seguimiento de asignaciones)
class AsignacionDeTarea(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)  # Conectando con Tarea
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Conectando con Usuario
    observaciones = models.TextField(max_length=300)
    fechaAsignacion = models.DateField()

# Modelo de Comentario
class Comentario(models.Model):
    contenido = models.TextField(max_length=300)
    fechaComentario = models.DateField()
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)

# Tabla intermedia para Usuarios y Proyectos
class Usuario_Proyecto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

# Tabla intermedia para Usuarios y Tareas
class Usuarios_Tareas(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)

# Tabla intermedia para Tareas y Etiquetas
class Tarea_Etiqueta(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)