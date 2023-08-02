from django.shortcuts import render
from apps.noticias.models import Post


def inicio(request):
    contexto ={}
    ultimas_tres = Post.objects.filter().order_by('-id')[:3]
    contexto['notis']= ultimas_tres
    
    template_name = 'inicio.html'
    return render(request, template_name, contexto)

def sobre_nosotros(request):
    template_name = 'sobre_nosotros.html'
    return render(request, template_name)