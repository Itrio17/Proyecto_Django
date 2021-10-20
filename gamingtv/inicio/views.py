from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User


# Create your views here.
@login_required()
def index(request):
    """ Atiende la petición GET / """
    return render(request, "inicioTv/index.html")


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
