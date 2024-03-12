# fifapp/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('crear_equipo/', views.crear_equipo, name='crear_equipo'),
    path('crear_posicion_juego/', views.crear_posicion_juego, name='crear_posicion_juego'),
    path('listar_posiciones_juego/', views.listar_posiciones_juego, name='listar_posiciones_juego'),
    path('crear_tecnico/', views.crear_tecnico, name='crear_tecnico'),
    path('listar_tecnicos/', views.listar_tecnicos, name='listar_tecnicos'),
    path('crear_jugador/', views.crear_jugador, name='crear_jugador'),
    path('listar_jugadores/', views.listar_jugadores, name='listar_jugadores'),
]

