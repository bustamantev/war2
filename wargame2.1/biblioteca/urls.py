from django.urls import path
from .views import  accion, battlesector, estrategia, form, index, spacemarine, spacemarine2, totalw3, videojuegos

urlpatterns = [
    path('accion', accion, name='accion'),
    path('battlesector', battlesector, name='battlesector'),
    path('estrategia', estrategia, name='estrategia'),
    path('form', form, name='form'),
    path('index', index, name='index'),
    path('spacemarine', spacemarine, name='spacemarine'),
    path('spacemarine2', spacemarine2, name='spacemarine2'),
    path('totalw3', totalw3, name='totalw3'),
    path('videojuegos', videojuegos, name='videojuegos')
]
