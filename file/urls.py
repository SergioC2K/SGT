"""URL's de importe del archivo"""

# Django
from django.urls import path

# Views
import file.views as ImporteControl
from . import views

urlpatterns = [
    path(
        route='importe/',
        view=ImporteControl.upload_excel,
        name='import'
    ),
    path(
        route='entregar/',
        view=views.ListarArchivo.as_view(),
        name='listar_llamada'
    ),
    path(
        route='asignar/',
        view=views.registro_llamada,
        name='asignar'
    ),
    path(
        route='realizar/',
        view=views.registro_llamada,
        name='registrar_llamada'
    ),
    path(
        route='buzon/',
        view=views.buzon,
        name='buzon'
    ),
    path(
        route='repartir/',
        view=views.repartir,
        name='repartir'
    ),
    path(
        route='enviar',
        view=views.enviarLlamadas,
        name='enviarLlamada'
    ),
    path(
        route='eliminar',
        view=views.archivoLlamadas,
        name='eliminar'
    ),

    path(
        route='entregar_l/',
        view=views.entregar.as_view(),
        name='entregar_l'
    ),
path(
        route='repartir/',
        view=views.repartir,
        name='repartir'
    ),
    path(
        route='enviar',
        view=views.enviarLlamadas,
        name='enviarLlamada'
    ),
path(
        route='entrega',
        view=views.ver_Llamadas,
        name='entrega'
    ),


]
