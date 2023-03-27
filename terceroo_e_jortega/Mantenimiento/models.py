from django.db import models

# Create your models here.
class Marcas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=100)

class Carros(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    modelo = models.CharField(max_length=100, unique=True, null=False)
    descripcion = models.TextField(null=False)
    precio = models.CharField(max_length=10, unique=True, null=False)
    disponibilidad = models.BooleanField(null=False, blank=False)
    marca = models.ForeignKey(Marcas, on_delete=models.PROTECT)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.descripcion, self.precio)