from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Modalidad(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    content = models.TextField(verbose_name='Contenido')
    slug = models.SlugField(verbose_name='Slug', default='', unique=True)
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  
    creator_id = models.ForeignKey(User, verbose_name="Creador", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    