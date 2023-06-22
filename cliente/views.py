from django.shortcuts import render

# Create your views here.

def main(request):
    context={}
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