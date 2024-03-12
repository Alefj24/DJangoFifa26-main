from django.db import models

# Create your models here.


class Equipo(models.Model):
    nombre = models.CharField(max_length=255)
    imagen_bandera = models.ImageField(upload_to='banderas/')
    escudo_equipo = models.ImageField(upload_to='escudos/')

    def __str__(self):
        return self.nombre

class PosicionJuego(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

from django.db import models
from .models import PosicionJuego

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='jugadores/')
    fecha_nacimiento = models.DateField()
    posicion = models.ForeignKey(PosicionJuego, on_delete=models.CASCADE)
    numero_camiseta = models.IntegerField()
    titular = models.BooleanField(default=False)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    
    
class Tecnico(models.Model):
    ROLES_CHOICES = [
        ('Técnico', 'Técnico'),
        ('Asistente', 'Asistente'),
        ('Médico', 'Médico'),
        ('Preparador Físico', 'Preparador Físico'),
    ]
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)
    rol = models.CharField(max_length=20, choices=ROLES_CHOICES)
    

    def __str__(self):
        return f"{self.nombre} {self.apellido}"