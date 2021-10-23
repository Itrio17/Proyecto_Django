from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile

# Create your views here.
@login_required()
def index(request):
    """ Atiende la petición GET / """
    return render(request, "inicioTv/index.html")


def catalogo(request):
    return render(request, "catalogo/catalogo.html")


def streamers(request):
    return render(request, "streamers/streamers.html")


def streamingroom(request):
    return render(request, "streamingroom/streamingroom.html")


def login_user(request):
    """ Atiende las peticiones de GET y POST /login/ """

    if request.method == "POST":
        # Se obtienen los datos del formulario
        user = request.POST["username"]
        passwd = request.POST["password"]
        next_ = request.GET.get("next", "/")
        user_obj = authenticate(username=user, password=passwd)
            # Tenemos usuario válido, redireccionamos a index
        if user_obj != None:
            #crea la sesion
            login(request, user_obj)
            #Usuario valido y se redirecciona a index
            return redirect(next_)
        else:
            # Usuario malo
            msg = "Datos incorrectos, intente de nuevo!"
    else:
        # Si no hay datos POST entonces es GET y enviamos formulario
        msg = ""

    return render(request, "registration/login.html",
        {
            "msg":msg,
        }
    )


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")

    return render(request, "registration/logout.html", {})


def register_user(request):
    """Atiende peticiones GET y POST de Registro"""
    if request.POST:
        username = request.POST.get("username")
        fechaNacimiento = request.POST.get("fechaNacimiento", None)
        if fechaNacimiento == "":
            fechaNacimiento = None
        email = request.POST.get("email", None)
        password1 = request.POST.get("password_1")
        password2 = request.POST.get("password_2")

        if password1 == password2:
            #modelo User
            user = User(
                username = username,
                email = email,
            )
            user.set_password(password1)
            user.save()
            #modelo Perfil
            perfil = Profile(
                user = user,
                fechaNacimiento = fechaNacimiento,
            )
            perfil.save()

            return redirect("/")
        else:
            msg = "ERROR: Las claves deben ser iguales"
    else:
        #atendiento GET
        msg=""

    return render(request, "registration/register.html", {
        "msg":msg
    })