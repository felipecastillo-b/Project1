from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template

class Person(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request):

    p1 = Person("Carlos Salvador", "Bilardo")
#    nombre = "Felipe"
#    apellido = "Castillo"
    ahora=datetime.datetime.now()
    temas_curso = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
#    doc_externo = open("./Project1/plantillas/plantilla.html")
#    plt = Template(doc_externo.read())
#    doc_externo.close()
#    ctx = Context({
#        "nombre_persona": p1.nombre,
#        "apellido_persona": p1.apellido,
#        "fecha_actual": ahora,
#        "temas": temas_curso
#        })

#    doc_externo = get_template("plantilla.html")

#    documento = doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "fecha_actual": ahora, "temas": temas_curso})

    return render(request, "plantilla.html", {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "fecha_actual": ahora, "temas": temas_curso})

def despedida(request):
        
    return HttpResponse("KKKKKKKKK")

def dameFecha(request):
    
    fecha_actual=datetime.datetime.now()
    
    document="""<html>
    <body>
    <h1>
    La Fecha %s
    </h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(document)

def calcularEdad(request, edad, anho):

    #edadActual=21
    periodo=anho-2023
    edadFutura=edad+periodo

    document="""<html>
    <body>
    <h1>
    En el año %s tu edad sera de %s años.
    </h1>
    </body>
    </html>""" %(anho, edadFutura) 

    return HttpResponse(document)

@csrf_exempt
def formularioNotas(request):

    return render(request, 'formulario.html')

@csrf_exempt
def informe(request):

    inf_nombre = str(request.POST['nombre'])
    inf_run = str(request.POST['run'])
    inf_carrera = str(request.POST['carrera'])
    inf_modulo = str(request.POST['modulo'])

    inf_nota1 = float (request.POST['nota1'])
    inf_nota2 = float (request.POST['nota2'])
    inf_nota3 = float (request.POST['nota3'])
    inf_nota4 = float (request.POST['nota4'])
    inf_nota5 = float (request.POST['nota5'])
    inf_nota6 = float (request.POST['nota6'])

    inf_promedio = round((inf_nota1*0.15)+(inf_nota2*0.15)+(inf_nota3*0.2)+(inf_nota4*0.2)+(inf_nota5*0.15)+(inf_nota6*0.15), 1)

    return render(request, "informe.html", {"inf_nota1": inf_nota1, "inf_nota2": inf_nota2, "inf_nota3": inf_nota3, "inf_nota4": inf_nota4, "inf_nota5": inf_nota5, "inf_nota6": inf_nota6, "inf_promedio": inf_promedio, "inf_nombre": inf_nombre, "inf_run": inf_run, "inf_carrera": inf_carrera, "inf_modulo": inf_modulo,})

def cursoC(request):

    fecha_actual=datetime.datetime.now()

    return render(request, "CursoC.html", {"dameFecha": fecha_actual})