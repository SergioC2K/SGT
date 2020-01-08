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
        route='entregar',
        view=views.listar_archivo.as_view(),
        name='listar_llamada'
    )
]
