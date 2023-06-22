from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .forms import clienteFormulario,ObrasFormulario
from django.contrib.auth.decorators import login_required
from .models import Obras,Estado

# Create your views here.

def main(request):
    context={}
    if request.user.is_autenticated :
        context["username"] = request.user.username
    return render(request, 'cliente/main.html', context)

def login(request):
    context={} 
    return render(request, 'cliente/login.html', context)

def login2(request):
    context={}
    return render(request, 'cliente/login2.html', context)

def registro(request):
    context={}
    return render(request, 'cliente/registro.html', context)

def miguelangel(request):
    context={}
    return render(request, 'cliente/miguelangel.html', context)

def pablopicasso(request):
    context={}
    return render(request, 'cliente/pablopicasso.html', context)

def vicentvangogh(request):
    context={}
    return render(request, 'cliente/vicentvangogh.html', context)

def artista(request):
    context={}
    return render(request, 'cliente/artista.html', context)

def obras(request):
    context={}
    return render(request, 'cliente/obras.html', context)

def base(request):
    context={}
    return render(request, 'cliente/base.html', context)