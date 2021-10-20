from typing import Tuple
from django.db import models

class User(models.Model):
    """Definición de la tabla User"""
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=80, null=True, blank=True)
    email = models.EmailField()
    fechaNacimiento = models.DateField(null=True, blank=True)
    clave = models.CharField(max_length=40, null=True, blank=True)
    tipo = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        """Representacion de str para User"""
        return self.nombre + " " + self.apellidos

class Registro(models.Model):
    nombre = models.Case