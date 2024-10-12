from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from novedades.models import Novedad

# Create your views here.
class HomePageView(ListView):
    model = Novedad
    template_name = 'core/home.html'
    
