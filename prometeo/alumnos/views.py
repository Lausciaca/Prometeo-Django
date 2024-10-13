from django.shortcuts import render
from django.views.generic.list import ListView


# Create your views here.
class CDEPageView(ListView):
    template_name = 'alumnos/centro_de_estudiantes.html'
    
class InscripcionesPageView(ListView):
    template_name = 'alumnos/inscripciones.html'
    
class ExamenesPageView(ListView):
    template_name = 'alumnos/examenes.html'
    
class HorariosPageView(ListView):
    template_name = 'alumnos/horarios.html'
    