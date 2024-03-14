from django.shortcuts import render, redirect
from .forms import EquipoForm, PosicionJuegoForm, TecnicoForm, JugadorForm, LoginForm, CustomUserCreationForm
from .models import Equipo, PosicionJuego, Tecnico, Jugador
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = EquipoForm() 
    Equipos=Equipo.objects.all()
    return render(request, 'fifapp/crear_equipo.html', {'form': form, 'Equipos': Equipos})

def home(request):
    return render(request, 'fifapp/index.html')  

def crear_posicion_juego(request):
    if request.method == 'POST':
        form = PosicionJuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
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
            return redirect('index')
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
            return redirect('index')
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


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('index')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'fifapp/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'fifapp/register.html', {'form': form})
