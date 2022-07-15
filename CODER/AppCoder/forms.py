from django import forms


class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    camada= forms.IntegerField()

class FormProf(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email= forms.EmailField()
    profesion = forms.CharField(max_length=50)

class Formestudiantes(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email= forms.EmailField()
