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
        route='contraseña/',
        view=views.cambio_contrasena,
        name='cambio'
    ),
    path(
        route='deshabilitar/',
        view=views.deshabilitar,
        name='desactivar'
    ),
    path(
        route='conexion/',
        view=views.deshabilitar,
        name='conectado'
    ),
]
