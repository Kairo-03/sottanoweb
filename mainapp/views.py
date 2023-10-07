from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def cargar_index(request):
    leer_template = loader.get_template("index.html")
    home = leer_template.render()
    return HttpResponse(home)


def login_form(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, "index.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "autenticacion/login.html", {"mensaje": "Error, datos incorrectos"})

        else:
            return render(request, "autenticacion/login.html", {"mensaje": "Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "autenticacion/login.html", {"form": form})


def register_form(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.changed_data['username']
            form.save()
            return render(request, "index.html", {"mensaje": "Usuario Creado"})

    else:
        form = UserCreationForm()

    return render(request, "autenticacion/register.html", {"form": form})
