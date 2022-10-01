from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
from AppFamiliares.models import Familiar

def crear_familiar(request):
    template = loader.get_template("templates.html")
    
    familiar_1 = Familiar(nombre="Nicolas", edad=27, email="nico@coder.com", fecha_nacim="1995-1-20")
    familiar_1.save()
    familiar_2 = Familiar(nombre="Ana", edad=23, email="ana@coder.com", fecha_nacim="1999-8-17")
    familiar_2.save()
    familiar_3 = Familiar(nombre="Virginia", edad=31, email="vir@coder.com", fecha_nacim="1991-4-11")
    familiar_3.save()

    dic_de_familiares = {
        "familiar_1" : familiar_1,
        "familiar_2" : familiar_2,
        "familiar_3" : familiar_3,
    }
    
    res = template.render(dic_de_familiares)
    
    return HttpResponse(res)
