from django.shortcuts import render, redirect
from .forms import EquipoForm, PosicionJuegoForm, TecnicoForm, JugadorForm
from .models import Equipo, PosicionJuego, Tecnico, Jugador

def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = EquipoForm() 
    Equipos=Equipo.objects.all()
    return render(request, 'fifapp/crear_equipo.html', {'form': form, 'Equipos': Equipos})

def home(request):
    return render(request, 'fifapp/home.html')  

def crear_posicion_juego(request):
    if request.method == 'POST':
        form = PosicionJuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_posiciones_juego') 
    else:
        form = PosicionJuegoForm()  
    return render(request, 'fifapp/crear_posicion_juego.html', {'form': form})

def listar_posiciones_juego(request):
    posiciones_juego = PosicionJuego.objects.all()
    return render(request, 'fifapp/listar_posiciones_juego.html', {'posiciones_juego': posiciones_juego})


def crear_tecnico(request):
    if request.method == 'POST':
        form = TecnicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tecnicos')
    else:
        form = TecnicoForm()
    return render(request, 'fifapp/crear_tecnico.html', {'form': form})

def listar_tecnicos(request):
    tecnicos = Tecnico.objects.all()
    return render(request, 'fifapp/listar_tecnicos.html', {'tecnicos': tecnicos})

def crear_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_jugadores')
    else:
        form = JugadorForm()
    return render(request, 'fifapp/crear_jugador.html', {'form': form})

def listar_jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'fifapp/listar_jugadores.html', {'jugadores': jugadores})

def index(request):
    equipos = Equipo.objects.all()
    jugadores = Jugador.objects.all()
    tecnicos = Tecnico.objects.all()
    return render(request, 'fifapp/index.html', {'equipos': equipos, 'jugadores': jugadores, 'tecnicos': tecnicos})