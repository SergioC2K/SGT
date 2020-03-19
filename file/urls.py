"""URL's de importe del archivo"""

# Django
from django.urls import path

# Views
import file.views as ImporteControl
from file import views

from .filters import RegistroLlamadaFilter

# Filtros
from django_filters.views import FilterView

urlpatterns = [
    path(
        route='importe/',
        view=ImporteControl.upload_excel,
        name='importe'
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
        view=views.realizar_llamada,
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
        route='entregar_l/',
        view=views.entregar.as_view(),
        name='entregar_l'
    ),
    path(
        route='entrega',
        view=views.ver_Llamadas,
        name='entrega'
    ),
    path(
        route='eliminar',
        view=views.archivoLlamadas.as_view(),
        name='eliminar'
    ),
    path(
      route='borrar',
      view=views.eliminarArchivo,
      name='exterminar'
    ),
    path(
        route='traer',
        view=views.traer,
        name='traer'
    ),
    path(
        route='ListFile',
        view=views.search,
        name='ListFile'
    ),
    path(
        route='verllamadas',
        view=views.ver_Llamadas,
        name='borrar'
    ),
    path(
        route='prueballamadas',
        view=views.pruebas_llamadas,
        name='prueballamada'
    ),
    path(
        route='prueba/<int:number>/',
        view=views.realizar_llamada,
        name='prueba'
    ),
    path(
        route='listfile',
        view=views.ListFile,
        name='listFile'
    ),
    path(
        route='estadito',
        view=views.CrearEstado.as_view(),
        name='estado'
    ),
    # esta ruta me retorna solo un template "reporte llamadas"
    path(
        route='reporte_llamada/',
        view=views.reporte_llamada,
        name='reporte_llamada'
    ),
    # esta ruta solo es para llevarle lo solicitado a el template"reporte llamadas"
    path(
        route='llevar_reporte_llamada',
        view=views.traer_reporte_llamada,
        name='llevar_reporte_llamada'
    ),
    path(
        route='completo',
        view=views.reporte_general,
        name='completo'
    )
]
