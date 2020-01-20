from django.urls import path

from usuario import views

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
        route='nuevo/',
        view=views.UserCreateView.as_view(),
        name='nuevo'
    ),
    path(
        route='registro/',
        view=views.UserCreateView.as_view(),
        name='signup'
    ),
    path(
        route='listar/',
        view=views.listar_usuario.as_view(),
        name='listar_usuario'
    ),

    path(
        route='perfil/',
        view=views.PerfilCreateView.as_view(),
        name='perfil'
    ),

    path(
        route='contrasena/',
        view=views.cambio_contrasena,
        name='cambio'
    ),
    path(
        route='deshabilitar/',
        view=views.deshabilitar,
        name='desactivar'
    ),
    path(
        route='eliminar/',
        view=views.deshabilitar,
        name='eliminar'
    ),
    path(
        route='con/',
        view=views.conectado,
        name='conexion'
    ),
    path(
        route='dis/',
        view=views.desconectado,
        name='desconexion'
    ),
]
