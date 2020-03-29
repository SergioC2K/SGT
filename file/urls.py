"""URL's de importe del archivo"""

# Django
from django.urls import path

# Views
import file.views as ImporteControl
from file import views

# Filtros

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
        route='create_estado',
        view=views.CrearEstado.as_view(),
        name='estado'
    ),

    path(
        route='update_estado',
        view=views.ActualizarEstado.as_view(),
        name='UpdateEstado'

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
    # esta ruta me lleva a el metodo donde se exporta para aceb
    path(
        route='completo',
        view=views.reporte_general,
        name='completo'
    ),
    # esta ruta me retorna los datos en el template "reporte general"
    path(
        route='envio_general',
        view=views.trer_reporte_general,
        name='envio_general'
    ),
    # esta ruta me retorna solo un template "reporte usuario"
    path(
        route='reporte_usuario',
        view=views.reporte_usuario,
        name='reporte_usuario'
    ),
    # esta ruta es para llevarle lo solicitado a el template"reporte usuario"
    path(
        route='traer_reporte_usuario',
        view=views.traer_reporte_usuario,
        name="traer_reporte_usuario"
    ),
    path(
        route='liquidacion_usuario',
        view=views.liquidacion_operador,
        name='liquidacion_usuario'
    ),
    path(
        route='llevar_liquidacion',
        view=views.llevar_liquidacion,
        name='llevar_liquidacion'
    )


]
