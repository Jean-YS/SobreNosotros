from django.db import models
class Grupo(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre del Grupo')
    descripcion = models.CharField(max_length=500, verbose_name='Descripcion')
    mision = models.CharField(max_length=500, verbose_name='Mision')
    vision = models.CharField(max_length=500, verbose_name='Vision')
    objetivos = models.CharField(max_length=500, verbose_name='Objetivos')
    def __str__(self):
        return self.nombre

# Create your models here.
