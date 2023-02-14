from django.shortcuts import render
from django.http import HttpResponse

from personas.models import Persona

# Create your views here.
def bienvenido(request):
    #return HttpResponse('Hola mundo desde Django')
    #mensajes={'msg1':'valor mensaje 1'}
    #return render(request,"bienvenido.html",mensajes)
    
    no_personas=Persona.objects.count()
    #personas=Persona.objects.all()
    personas=Persona.objects.order_by('id')#descendete -id
    return render(request,"bienvenido.html",{'no_personas': no_personas ,'personitas': personas})

def despedirse(request):
    return HttpResponse('despdida desde Django')


def contacto(request):
    nombre='hola'
    numero=4
    return HttpResponse(f'nombre: {nombre} numero:{numero} ')
