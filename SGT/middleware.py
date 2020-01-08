"""Platzigram middleware catalog."""

# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompleteMiddleware:
    """
    Middleware que se encarga de restringir el acceso
    si el usuario no tiene el los datos completos
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                perfil = request.user.perfil
                if not perfil.cedula \
                        and not perfil.telefono_fijo \
                        and not perfil.celular \
                        and not perfil.celular_telemercadeo:
                    if request.path not in [reverse('usuario:perfil'), reverse('usuario:logout')]:
                        return redirect('usuario:perfil')

        response = self.get_response(request)
        return response
