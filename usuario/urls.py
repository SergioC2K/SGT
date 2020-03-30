from django.urls import path

from usuario import views

urlpatterns = [

    path(
        route='login/',
        view=views.LoginViewUsuario.as_view(),
        name='login'
    ),
    path(
        route='cambio-contrasena/',
        view=views.cambio_contrasena,
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
        route='actualizar',
        view=views.actualizarUsu.as_view(),
        name='actualizar'
    ),
    path(
        route='notichecked',
        view=views.notificaciones_checked,
        name='notichecked'
    ),
]
