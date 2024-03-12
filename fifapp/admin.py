from django.contrib import admin
from .models import Equipo, Jugador, PosicionJuego, Tecnico

admin.site.register(Equipo)
admin.site.register(Jugador)
admin.site.register(PosicionJuego)
admin.site.register(Tecnico)
