from django.shortcuts import render
from django.views.generic.list import ListView
from .models import CDE, Inscripcion, Examen, Horario


# Create your views here.
class CDEPageView(ListView):
    model = CDE
    template_name = 'alumnos/centro_de_estudiantes.html'
    
class InscripcionesPageView(ListView):
    model = Inscripcion
    template_name = 'alumnos/inscripciones.html'
    
class ExamenesPageView(ListView):
    model = Examen
    template_name = 'alumnos/examenes.html'
    
class HorariosPageView(ListView):
    model = Horario
    template_name = 'alumnos/horarios.html'
    