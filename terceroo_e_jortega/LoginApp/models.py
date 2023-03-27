from django.db import models

# Create your models here.
class Ciudades(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(null=False, unique=True, max_length=100)

class Generos(models.Model):
    id = models.AutoField(primary_key=True)
    genero = models.CharField(null=False, unique=True, max_length=100)

class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(null=False, max_length=256)
    correo = models.CharField(null=False, unique=True, max_length=256)
    ciudad = models.ForeignKey(Ciudades, on_delete=models.PROTECT, default=False)
    genero = models.ForeignKey(Generos, on_delete=models.PROTECT, default=False)
    usuario = models.CharField(null=False, unique=True, max_length=100)
    contrasena = models.CharField(null=False, blank=False, max_length=150)