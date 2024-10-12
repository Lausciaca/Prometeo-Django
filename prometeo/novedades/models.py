from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Novedad(models.Model):
    title= models.CharField(max_length=100,  verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)
    order = models.IntegerField(verbose_name='Orden', default=0)
    creator_id = models.ForeignKey(User, verbose_name="Creador", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    