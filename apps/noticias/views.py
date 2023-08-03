from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Categorias, Post
from apps.opiniones.models import Opinion
from apps.opiniones.forms import OpinionForm


# Create your views here.

class AgragarCategoria(CreateView, LoginRequiredMixin):
    model = Categorias
    fields = ['nombre']
    template_name = 'noticias/agregar_categoria.html'
    success_url = reverse_lazy('inicio')
    
'''class BorrarCategoria(LoginRequiredMixin, DeleteView):
    model = Categorias
    template_name = 'noticias/eliminar_categoria.html'
    success_url = reverse_lazy('apps.noticias:listar_post')

    def get_context_data(self, kwargs):
        context = super().get_context_data(kwargs)
        context['titulo'] = 'Eliminar Categoría' 
        # podes cambiar el titulo por el parametro que necesitas
        return context'''
    

    
class AgragarPost(CreateView, LoginRequiredMixin):
    model = Post
    fields = ['titulo', 'autor', 'contendio', 'categoria', 'imagen']
    template_name = 'noticias/agregar_post.html'
    success_url = reverse_lazy('inicio')
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.colaborador = self.request.user
        return super().form_valid(form)
    
class ModificarPost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['titulo', 'autor', 'contendio', 'categoria', 'imagen']
    template_name = 'noticias/agregar_post.html'
    success_url = reverse_lazy('apps.noticias:listar_post')
    
class EliminarPost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'noticias/confirma_eliminar.html'
    success_url = reverse_lazy('apps.noticias:listar_post')
    
    
    
class ListarPost(ListView): 
    model = Post
    template_name = 'noticias/listar_post.html' 
    context_object_name = 'post' 
    
    def get_context_data(self):
        context = super().get_context_data()  
        categorias = Categorias.objects.all() 
        context['categorias'] = categorias
        return context 
    
    def get_queryset(self):
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(titulo__icontains=query)  

        return queryset.order_by('titulo')
    

def ListarPostPorCategoria(request,categoria):
    categorias2 = Categorias.objects.filter(nombre=categoria)
    post = Post.objects.filter(categoria= categorias2[0].id).order_by('fecha_agragado')
    template_name = 'noticias/listar_post.html'
    categorias = Categorias.objects.all()
    contexto = {
        'post': post,
        'categorias': categorias
    }
    return render(request, template_name, contexto)
    

#class PostDetalle(DetailView):
    #model = Post
    #template_name = 'noticias/post.html'  
    #context_object_name = 'post' 
    
def post_detalle(request, id):
    post = Post.objects.get(id=id)
    opiniones = Opinion.objects.filter(noticia=post)
    
    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                opinion = form.save(commit=False)
                opinion.noticia = post
                opinion.usuario = request.user
                opinion.save()
                form = OpinionForm()
            else:
                return redirect('apps.usuarios:iniciar_sesion')
    else:
        form = OpinionForm()
        
    contexto ={
        'post': post,
        'form': form,
        'opiniones': opiniones,
    }
    template_name = 'noticias/post.html'
    return render(request, template_name, contexto)

            
        
