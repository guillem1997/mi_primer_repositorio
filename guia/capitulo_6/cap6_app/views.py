from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def anadir(request):
    prioridad = request.POST["name_prioridad"]
    titulo = request.POST["name_titulo"]
    nota = request.POST["name_nota"]
    return (HttpResponse(f'Insertado <br> '
                         f'prioridad: {prioridad}<br>'
                         f'titulo: {titulo}<br>'
                         f'nota: {nota}<br>'))
# Create your views here.
