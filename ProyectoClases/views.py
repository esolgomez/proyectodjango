from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random

from Home.models import persona

def hola(request):
    return HttpResponse('<h1>Holaaaaaaaa!!!!</h1>')

def fecha(request):
    fecha_y_hora = datetime.now() 
    return HttpResponse(f'La hora y fecha actual es {fecha_y_hora}')

def calcular_fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Tu fecha de nacimiento aproximada para tus {edad} años seria: {fecha}')

def mi_template(request):
    
    cargar_archivo = open(r'C:\Users\cj286xu\OneDrive - EY\Desktop\Django 2\proyectoDjango\ProyectoClases\templates\mi_template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)

def tu_template(request, nombre):
    
    template = loader.get_template('tu_template.html')
    template_renderizado = template.render({'persona': nombre})
    
    return HttpResponse(template_renderizado)

def pruba_template(request):
    mi_contexto = {
        'rango': list(range(1,11)),
        'valor_aleatorio': random.randrange(1,11)
    }
    template = loader.get_template('prueba_template.html')
    template_renderizado = template.render(mi_contexto)
    
    return HttpResponse(template_renderizado)


def crear_persona(request, nombre, apellido):
    Persona = persona(nombre=nombre, apellido=apellido, edad=random.randrange(1, 99), fecha_nacimiento=datetime.now())
    Persona.save()
    template = loader.get_template('crear_persona.html')
    template_renderizado = template.render({'Persona': persona})
    return HttpResponse(template_renderizado)

def ver_personas(request):
    personas = persona.objects.all
    template = loader.get_template('ver_personas.html')
    template_renderizado = template.render({'Personas': personas})
    return HttpResponse(template_renderizado)