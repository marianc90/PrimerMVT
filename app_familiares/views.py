from logging.config import dictConfig
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from app_familiares.models import Familiares

def consulta_familiares(request):
    plantilla = get_template('familiares.html')
    familiares = Familiares.objects.all()
    diccionario = {'familiares': familiares}
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

# Create your views here.
