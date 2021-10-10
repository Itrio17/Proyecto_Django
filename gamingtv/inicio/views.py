from django.shortcuts import render

# Create your views here.
def index(request):
    """Vista para atender la peticion de la url"""
    return render(request, "inicioTv/index.html")