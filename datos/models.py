from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_de_nacimiento = models.DateField(null = True, blank = True)
    Genero = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    estado_civil = models.CharField(max_length=50)
    dpi = models.CharField(max_length=13)