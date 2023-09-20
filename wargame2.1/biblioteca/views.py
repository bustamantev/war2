from django.shortcuts import render

# Create your views here.

def accion(request):
    return render(request, 'Accion.html')

def battlesector(request):
    return render(request, 'battlesector.html')

def estrategia(request):
    return render(request, 'Estrategia.html')

def form(request):
    return render(request, 'form.html')

def index(request):
    return render(request, 'index.html')

def spacemarine(request):
    return render(request, 'spacemarine.html')

def spacemarine2(request):
    return render(request, 'spacemarine2.html')

def totalw3(request):
    return render(request, 'totalw3.html')

def videojuegos(request):
    return render(request, 'videojuegos.html')


