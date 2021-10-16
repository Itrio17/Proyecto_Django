from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
# Create your views here.
def index(request):
    """Vista para atender la peticion de la url"""
    return render(request, "inicioTv/index.html")