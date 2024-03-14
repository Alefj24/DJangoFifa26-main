from django import forms
from .models import Equipo, PosicionJuego, Tecnico, Jugador
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'imagen_bandera', 'escudo_equipo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen_bandera': forms.FileInput(attrs={'class': 'form-control-file'}),
            'escudo_equipo': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

class PosicionJuegoForm(forms.ModelForm):
    class Meta:
        model = PosicionJuego
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }
        

class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'nacionalidad', 'rol']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }


class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'apellido', 'foto', 'fecha_nacimiento', 'posicion', 'numero_camiseta', 'titular', 'equipo']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User name / Email', 'class': 'Login-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'Login-input'}))

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']