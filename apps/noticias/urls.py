from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from .views import*

app_name = 'apps.noticias'

urlpatterns = [
    path('agregar_categoria', AgragarCategoria.as_view(), name='agregar_categoria'),
    path('agregar_post/', AgragarPost.as_view(), name='agregar_post'),
    path('modificar_post/<int:pk>', ModificarPost.as_view(), name='modificar_post'),
    path('eliminar_post/<int:pk>', EliminarPost.as_view(), name='eliminar_post'),
    path('listar_post/', ListarPost.as_view (), name='listar_post' ),
    path('listar_por_categoria/<str:categoria>', ListarPostPorCategoria, name='listar_por_categoria' ),
    path('post_detalle/<int:id>', post_detalle, name='post_detalle'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
