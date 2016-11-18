from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create your models here.

class Libro(models.Model):
    isbn = models.CharField(max_length=13)
    titulo = models.CharField(max_length=60)
    imagen = models.FileField(null=True, blank=True)
    autor = models.CharField(max_length=60)
    editorial = models.CharField(max_length=60)
    pais = models.CharField(max_length=30)
    anio = models.IntegerField()
    def __str__(self):
        return self.isbn

class Cliente(models.Model):
    isbn = models.CharField(max_length=13)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.dpi

class Prestamo(models.Model):
    fecha_prestamo = models.DateTimeField(default=timezone.now)
    fecha_devolucion_previsto = models.DateTimeField()
    fecha_devolucion_real = models.DateTimeField()
    cliente = models.ForeignKey(Cliente)
    libro = models.ManyToManyField(Libro)
