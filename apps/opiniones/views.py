from typing import Any
from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView

from .models import Opinion
from .forms import OpinionForm


# Create your views here.

def AgregarOpinion(request):
    form = OpinionForm(request.POST)
    if form.is_valid():
        form.save()
        form = OpinionForm
        
    contexto ={
        'form' : form,
    }
    template_name = 'opiniones/agregar_opinion.html'
    return render(request, template_name, contexto)


class ModificarOpinion(LoginRequiredMixin, UpdateView):
    model = Opinion
    fields = ['texto']
    template_name = 'opiniones/agregar_opinion.html'
    success_url = reverse_lazy('apps.noticias:listar_post')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(usuario = self.request.user)
    
class EliminarOpinion(LoginRequiredMixin, DeleteView):
    model = Opinion
    template_name = 'noticias/confirma_eliminar.html'
    success_url = reverse_lazy('apps.noticias:listar_post')