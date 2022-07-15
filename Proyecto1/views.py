from django.http import HttpResponse
from django.template import loader

def saludo(request):
    return HttpResponse("Hola")

def probandoTemp(self):
    
    nombre = "Thomas"
    apellido = "Solis"

    diccionario={"nombre":nombre, "apellido": apellido}

    plantilla= loader.get_template("template1.html")
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
