from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import update_session_auth_hash
from .form import UserRegisterForm, UserEditForm
from .models import Avatar, Contenido
# Create your views here.


def cargar_avatar(request):
    avatar = Avatar.objects.filter(user=request.user.id).first()
    return avatar


def cargar_index(request):
    avatar = cargar_avatar(request)
    es_staff = request.user.groups.filter(name='staff').exists()
    return render(request, "index.html", {'es_staff': es_staff, 'avatar': avatar})


def cargar_servicios(request):
    avatar = cargar_avatar(request)
    contenidos = Contenido.objects.all()
    return render(request, 'servicios.html', {'contenidos': contenidos, 'avatar': avatar})


def login_form(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            login(request, form.get_user())
            return render(request, "index.html", {"mensaje": f"Bienvenido {usuario}"})
    else:
        form = AuthenticationForm()

    return render(request, "autenticacion/login.html", {"form": form})


def register_form(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            return render(request, "autenticacion/login.html", {"mensaje": f"Usuario {username} creado con éxito."})
    else:
        form = UserRegisterForm()

    return render(request, "autenticacion/register.html", {"form": form})


@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.set_password(informacion['password1'])
            usuario.save()
            update_session_auth_hash(request, usuario)

            return redirect("home")
    else:
        miFormulario = UserEditForm(initial={
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name
        })

    return render(request, "autenticacion/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
