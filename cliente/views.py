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
    if request.user.is_authenticated :
        context["username"] = request.user.username
    return render(request, 'cliente/main.html', context)

def login2(request):
    if request.method == "POST":
        context={}
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            return redirect(listaObra)
        else:
            return render(request, 'cliente/login2.html', context)
    else:
        context={}
    return render(request, 'cliente/login2.html', context)

def registro(request):
    if request.method == 'POST':
        context={}
        try:
            if request.POST["password1"] == request.POST["password2"]:
                form = User.objects.create_user(username=request.POST["username"],password=request.POST["password1"],is_active=True)
                form.save()
                return redirect(perfil)
            else:
                formulario = UserCreationForm()
                context["form"] = formulario
            return render(request, 'cliente/registro.html', context)
        except:
            formulario = UserCreationForm()
            context["form"] = formulario
            return render(request, 'cliente/registro.html', context)
    else:
        context={}
        formulario = UserCreationForm()
        context["form"] = formulario
        return render(request, 'cliente/registro.html', context)

def miguelangel(request):
    context={}
    if request.user.is_authenticated :
        context["username"] = request.user.username
    articulos = Obras.objects.filter(idUsuario=request.user)
    context["articulos"] = articulos
    return render(request, 'cliente/miguelangel.html', context)

def pablopicasso(request):
    context={}
    if request.user.is_authenticated :
        context["username"] = request.user.username
    articulos = Obras.objects.filter(idUsuario=request.user)
    context["articulos"] = articulos
    return render(request, 'cliente/pablopicasso.html', context)

def vicentvangogh(request):
    context={}
    if request.user.is_authenticated :
        context["username"] = request.user.username
    articulos = Obras.objects.filter(idUsuario=request.user)
    context["articulos"] = articulos
    return render(request, 'cliente/vicentvangogh.html', context)

def artista(request):
    context={}
    return render(request, 'cliente/artista.html', context)

def obras(request):
    context={}
    return render(request, 'cliente/obras.html', context)

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect(main)

@login_required
def cambio_pass(request):
    context={}
    if request.user.is_autenticated :
        context["username"] = request.user.username
    return render(request, 'cliente/cambio_pass.html', context)

def recuperar_pass(request):
    return redirect(main)

@login_required
def perfil(request):
    context={}
    if request.method == 'POST':
        try:
            context
            if request.user.is_authenticated :
                context["username"] = request.user.username
                
            usuario = User.objects.get(username=request.user.username)
            formulario = clienteFormulario(request.POST, instance=usuario)
            formulario.save()
            return redirect(main)
        except:
            if request.user.is_authenticated :
                context["username"] = request.user.username

            usuario = User.objects.get(username=request.user.username)
            formulario = clienteFormulario(instance=usuario)
            context["formulario"] = formulario
            return render(request, 'cliente/perfil.html', context)
    else:
        if request.user.is_authenticated :
            context["username"] = request.user.username

        usuario = User.objects.get(username=request.user.username)
        formulario = clienteFormulario(instance=usuario)
        context["formulario"] = formulario
        return render(request, 'cliente/perfil.html', context)

@login_required
def listaObra(request):
    context={}
    if request.user.is_authenticated :
        context["username"] = request.user.username
    articulos = Obras.objects.filter(idUsuario=request.user)
    context["articulos"] = articulos
    return render(request, 'cliente/listaObra.html',context)

@login_required
def agregarObra(request):
    context={}
    if request.user.is_authenticated :
        context["username"] = request.user.username
    if request.method == "POST":
        estado = Estado.objects.get(idEstado='1')
        form = ObrasFormulario(request.POST,request.FILES)        
        if form.is_valid():
            Obras_f =  form.save(commit=False) #este me tinca que tiene algo que revisar
            Obras_f.idUsuario = request.user
            form.save()
            
            return redirect(listaObra)
        else:
            print(form.errors)
            Obras = ObrasFormulario(instance=estado)
            context["formulario"] = Obras
            return render(request, 'cliente/agregarObra.html', context)
    else:
        Obras = ObrasFormulario()
        context["formulario"] = Obras
        return render(request, 'cliente/agregarObra.html', context)
    

@login_required #este tambien hay que revisarlo esta dando error en los artistas
def editarObra(request, idObras):
    try:
        obra = Obras.objects.get(id_obra=idObras)
        context ={}
        if obra:
            if request.method == "POST":
                form = ObrasFormulario(request.POST, instance = obra)
                form.save()
                context ={'Obras':obra}
                return render(request, 'cliente/editar_obra.html', context)
            else:
                form = ObrasFormulario(instance = obra)
                context={'obra':obra}
                return render(request, 'cliente/listaObra.html', context)
    except:
        obra = Obras.objects.all()
        mensaje = "Error"
        context = {'obra':obra, 'mensaje':mensaje}
        return render(request, 'cliente/listaObra.html', context)
    return redirect(editarObra)