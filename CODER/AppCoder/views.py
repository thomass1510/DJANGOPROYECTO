from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor, Estudiante
from AppCoder.forms import CursoForm, FormProf, Formestudiantes

# Create your views here.

def curso(self):

    curso=Curso(nombre = 'Django', camada = '9393939')
    curso.save()
    doc = f"Curso {curso.nombre} camada {curso.camada}"

    return HttpResponse(doc)

def inicio(request):

    return render(request, "AppCoder/inicio.html")


def formestudiantes(request):

    if request.method == "POST":

        form=Formestudiantes(request.POST)  
        print(form)
        if form.is_valid:

            info = form.cleaned_data
            nombre = info['nombre']
            apellido = info['apellido']
            email = info['email']
            estudiante = Estudiante (nombre=nombre, apellido=apellido,email=email)
            estudiante.save()
            return render(request, "AppCoder/inicio.html")

    else:
        form = Formestudiantes()
    return render(request, "AppCoder/estudiantes.html", {"formulario":form})

def cursoForm(request):

    if request.method == "POST":

        form=CursoForm(request.POST)  
        print(form)
        if form.is_valid:

            info = form.cleaned_data
            nombre = info['nombre']
            camada = info['camada']
            curso = Curso (nombre=nombre, camada=camada)
            curso.save()
            return render(request, "AppCoder/inicio.html")

    else:
        form = CursoForm()
    return render(request, "AppCoder/cursos.html", {"formulario":form})

def formProfe(request):

    if request.method == "POST":

        form=FormProf(request.POST)  
        print(form)
        if form.is_valid:

            info = form.cleaned_data
            nombre = info['nombre']
            apellido = info['apellido']
            email = info['email']
            profesion = info['profesion']
            profesor = Profesor (nombre=nombre, apellido=apellido,email=email,profesion=profesion)
            profesor.save()
            return render(request, "AppCoder/inicio.html")

    else:
        form = FormProf()
    return render(request, "AppCoder/profesores.html", {"formulario":form})


def busquedaCamada(request):

    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
    if request.GET['camada']:

        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos":cursos, "camada": camada})
    else:   
        return render(request, "AppCoder/busquedaCamada.html", {"error": "NO se ingreso ninguna camada"})
    