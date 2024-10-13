from django.shortcuts import render
from .models import Libro
from materias.models import Materia
from django.views.generic.list import ListView

# Create your views here.
class LibrosListView(ListView):
    model = Libro
    template_name = 'libros/biblioteca.html'
    context_object_name = 'libros'
    
    def get_context_data(self, **kwargs):
        # Primero llama al contexto base proporcionado por ListView
        context = super().get_context_data(**kwargs)
        
        # Agregar otros modelos al contexto
        context['autores'] = Libro.objects.values_list('author', flat=True).distinct()[:10]
        context['materias'] = Materia.objects.all()  # Por ejemplo, lista de materias
        
        return context