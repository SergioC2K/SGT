from django.urls import path, include

from usuario import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path(
        route='login/',
        view=views.LoginViewUsuario.as_view(),
        name='login'
    ),
    path(
        route='cambio-contrasena/',
        view=auth_views.
            PasswordChangeView.as_view(
            template_name='users/nuevaContrasena.html'
        ),
        name='cambio'
    ),
    path(
        route='logout/',
        view=views.logout_view,
        name='logout'
    ),

    path(
        route='registro/',
        view=views.UserCreateView,
        name='signup'
    ),
    path(
        route='listar/',
        view=views.ListarUsuario.as_view(),
        name='listar_usuario'
    ),
    path(
        route='perfil/',
        view=views.UpdateProfileView.as_view(),
        name='perfil'
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
    path(
        route='prueba/<perfil>/',
        view=views.UpdateProfileView.as_view(),
        name='desconexion'
    ),
]
