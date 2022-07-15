from django.urls import path
from .views import *


urlpatterns = [
    path ('', inicio, name = 'inicio'),
    path ('cursos/', cursoForm, name = 'cursos'),
    path ('entregables/', entregables, name = 'entregables'),
    path ('profesores/', formProfe, name = 'profesores'),
    path ('estudiantes/', formestudiantes, name = 'estudiantes'),
    path ('busquedaCamada/', busquedaCamada, name = 'busquedaCamada'),
    path ('buscar/', buscar),
]