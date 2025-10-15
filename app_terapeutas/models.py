from django.db import models

class Terapeuta(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f'Terapeuta: {self.nombre} {self.apellido}'

