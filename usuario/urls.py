from django.urls import path

from . import views

urlpatterns = [

    path(
        '',
        views.login_view,
        name='login'
     ),

    path(
        route='logout/',
        view=views.logout_view,
        name='logout'
    ),

    path(
        route='signup/',
        view=views.registrar,
        name='signup'
    ),
    path(
        route='listar/',
        view=views.listar_usuario.as_view(),
        name='listar_usuario'
    ),

    path(
        route='perfil/',
        view=views.actualizar_usuario,
        name='perfil'
    ),

    path(
        route='contraseña/',
        view=views.cambio_contraseña,
        name='cambio'
    ),

    path(
        route='deshabilitar/<id>',
        view=views.deshabilitar,
        name='desactivar'
    ),



]
