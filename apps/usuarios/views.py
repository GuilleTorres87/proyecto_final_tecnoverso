from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Usuarios
from .forms import RegistrarUsuarioForm
from django.http import HttpResponse

# Create your views here.

class RegistrarUsuario(CreateView):
    models = Usuarios
    template_name = 'usuarios/registrar.html'
    form_class = RegistrarUsuarioForm
    success_url = reverse_lazy('inicio')
    
class EliminarUsuario(LoginRequiredMixin, DeleteView):
    model = Usuarios
    template_name = 'usuarios/confirma_eliminar.html'
    success_url = reverse_lazy('apps.usuarios:listar_usuarios')    
    
    
def ListarUsuarios(request):
    usuarios =Usuarios.objects.all()
    template_name ='usuarios/listar_usuarios.html'
    contexto= {
        'usuarios': usuarios
    }
    return render(request, template_name, contexto)    
    
    
    
