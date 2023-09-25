from django.http import HttpResponse
import datetime
from django.template import Template, Context

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

    doc_externo = open("./Project1/plantillas/plantilla.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({
        "nombre_persona": p1.nombre,
        "apellido_persona": p1.apellido,
        "fecha_actual": ahora,
        "temas": temas_curso
        })

    documento = plt.render(ctx)

    return HttpResponse(documento)

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

def formularioNotas(request):

    doc_externo = open("C:/Users/Usuario_2/Documents/FELIPE/workspace/.Proyectos_Django/Project1/Project1/plantillas/formulario.html")

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context()

    documento = plt.render(ctx)

    return HttpResponse(documento)