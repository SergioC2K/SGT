# Django
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from file import views
from usuario import views


urlpatterns = [


    path(
        '',
        views.login_view,
        name='inicio'
     ),
    path('archivo/', include(('file.urls', 'file'), namespace='archivo')),
    path('usuario/', include(('usuario.urls', 'usuario'), namespace='usuario'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
