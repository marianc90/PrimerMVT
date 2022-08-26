from django.db import models

class Familiares(models.Model):
    nombre = models.CharField(max_length=128)
    apellido= models.CharField(max_length=128)
    telefono = models.IntegerField()
    fecha_nacimiento=models.DateField()
# Create your models here.
