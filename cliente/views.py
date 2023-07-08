from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .forms import clienteFormulario,ObrasFormulario, actualizar
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Obras,Estado

# Create your views here.
def superusuario(user):
    return user.is_superuser

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
            return redirect(main)
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
                return redirect(main)
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
    if request.method =='POST':
        context={}
        if request.user.is_authenticated :
            context["username"] = request.user.username
        filtro =request.POST['filtro']
        print(filtro)
        if filtro != 'todo':
            user = User.objects.get(username='MiguelAngel')
            user_id = user.id
            articulos = Obras.objects.filter(idUsuario=user_id, estado=1, tipo=filtro)
            context["articulos"] = articulos
            return render(request, 'cliente/miguelangel.html', context)
        else:
            user = User.objects.get(username='MiguelAngel')
            user_id = user.id
            articulos = Obras.objects.filter(idUsuario=user_id, estado=1)
            context["articulos"] = articulos
            return render(request, 'cliente/miguelangel.html', context)
    else:
        context={}
        if request.user.is_authenticated :
            context["username"] = request.user.username
        user = User.objects.get(username='MiguelAngel')
        user_id = user.id
        articulos = Obras.objects.filter(idUsuario=user_id, estado=1)
        context["articulos"] = articulos
        return render(request, 'cliente/miguelangel.html', context)

def pablopicasso(request):
    if request.method =='POST':
        context={}
        if request.user.is_authenticated :
            context["username"] = request.user.username
        filtro =request.POST['filtro']
        print(filtro)
        if filtro != 'todo':
            user = User.objects.get(username='PabloPicasso')
            user_id = user.id
            articulos = Obras.objects.filter(idUsuario=user_id, estado=1, tipo=filtro)
            context["articulos"] = articulos
            return render(request, 'cliente/pablopicasso.html', context)
        else:
            user = User.objects.get(username='PabloPicasso')
            user_id = user.id
            articulos = Obras.objects.filter(idUsuario=user_id, estado=1)
            context["articulos"] = articulos
            return render(request, 'cliente/pablopicasso.html', context)
    else:
        context={}
        if request.user.is_authenticated :
            context["username"] = request.user.username
        user = User.objects.get(username='PabloPicasso')
        user_id = user.id
        articulos = Obras.objects.filter(idUsuario=user_id, estado=1)
        context["articulos"] = articulos
        return render(request, 'cliente/pablopicasso.html', context)

def vicentvangogh(request):
    if request.method =='POST':
        context={}
        if request.user.is_authenticated :
            context["username"] = request.user.username
        filtro =request.POST['filtro']
        print(filtro)
        if filtro != 'todo':
            user = User.objects.get(username='VincentVanGogh')
            user_id = user.id
            articulos = Obras.objects.filter(idUsuario=user_id, estado=1, tipo=filtro)
            context["articulos"] = articulos
            return render(request, 'cliente/vicentvangogh.html', context)
        else:
            user = User.objects.get(username='VincentVanGogh')
            user_id = user.id
            articulos = Obras.objects.filter(idUsuario=user_id, estado=1)
            context["articulos"] = articulos
            return render(request, 'cliente/vicentvangogh.html', context)
    else:
        context={}
        if request.user.is_authenticated :
            context["username"] = request.user.username
        user = User.objects.get(username='VincentVanGogh')
        user_id = user.id
        articulos = Obras.objects.filter(idUsuario=user_id, estado=1)
        context["articulos"] = articulos
        return render(request, 'cliente/vicentvangogh.html', context)

def artista(request):
    context={}
    return render(request, 'cliente/artista.html', context)

def obras(request):
    context={}
    return render(request, 'cliente/obras.html', context)

def todo(request):
    if request.method =='POST':
        context={}
        if request.user.is_authenticated :
            context["username"] = request.user.username
        filtro =request.POST['filtro']
        print(filtro)
        if filtro != 'todo':
            articulos = Obras.objects.filter(estado=1, tipo=filtro)
            context["articulos"] = articulos
            return render(request, 'cliente/todo.html', context)
        else:
            articulos = Obras.objects.filter(estado=1)
            context["articulos"] = articulos
            return render(request, 'cliente/todo.html', context)
    else:
        context={}
        if request.user.is_authenticated :
            context["username"] = request.user.username
        articulos = Obras.objects.filter(estado=1)
        context["articulos"] = articulos
        return render(request, 'cliente/todo.html', context)

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
            Obra =  form.save(commit=False) 
            Obra.idUsuario = request.user
            Obra.save()
            
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
def editarObra(request, idObra):
    context = {}
    obra = get_object_or_404(Obras,pk=idObra)
    if request.method == 'POST':
        arte = ObrasFormulario(request.POST, instance=obra)
        if arte.is_valid():
            estado_default = Estado.objects.all()[1] 
            arte.instance.mensaje = Obras._meta.get_field('mensaje').get_default()
            arte.instance.estado = estado_default
            arte.save()
            return redirect(listaObra)
    else:
        arte = ObrasFormulario(instance=obra)
    
    context["formulario"] = arte
    return render(request, 'cliente/editar_obra.html', context)

@user_passes_test(superusuario)
def actualizar_obra(request):
    context={}
    if request.user.is_authenticated :
        context["username"] = request.user.username
    return render(request, 'cliente/admin.html',context)

@user_passes_test(superusuario)
def admin(request):
    context={}
    if request.user.is_authenticated :
        context["username"] = request.user.username
    if request.method == "POST":
        idobra = request.POST['idobra']
        dato = request.POST['estado']
        mensaje = request.POST['mensaje']
        obra = Obras.objects.get(idObras=idobra)
        estado = Estado.objects.get(estado=dato)
        obra.estado = estado
        obra.mensaje = mensaje
        obra.save()
        redirect(admin)
    articulos = Obras.objects.filter(estado=2)
    estado_obra = Estado.objects.all()
    context = {'articulos':articulos, 'estado_obra':estado_obra}
    return render(request, 'cliente/admin.html', context)