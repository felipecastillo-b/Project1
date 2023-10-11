from django import forms

class formularioAlumno(forms.Form):
    nombre = forms.CharField()
    run = forms.CharField()
    carrera = forms.CharField()
    nota1 = forms.DecimalField()
    nota2 = forms.DecimalField()
    nota3 = forms.DecimalField()
    nota4 = forms.DecimalField()
    nota5 = forms.DecimalField()
    nota6 = forms.DecimalField()
    modulo = forms.CharField()