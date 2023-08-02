from django.db import models
from django.utils import timezone
from apps.usuarios.models import Usuarios

# Create your models here.
class Categorias(models.Model):
    nombre = models.CharField(max_length=20, null=False)
    
    def __str__(self):
        return self.nombre
    
    

class Post(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    autor = models.CharField(max_length=20, null=False)
    contendio = models.TextField()
    slug = models.SlugField()
    fecha_agragado = models.DateTimeField(auto_now_add=True)
    colaborador = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True)
    published = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(null=True, blank=True, upload_to='noticias', default='noticias/noticia_default.png')
    categoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ('-published',)
    
