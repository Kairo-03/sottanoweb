from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .form import UserRegisterForm
from .models import Contenido
# Create your views here.


def cargar_index(request):
    es_staff = request.user.groups.filter(name='staff').exists()
    return render(request, "index.html", {'es_staff': es_staff})


def cargar_servicios(request):
    contenidos = Contenido.objects.all()
    return render(request, 'servicios.html', {'contenidos': contenidos})


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
