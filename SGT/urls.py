
from django.urls import path, include


urlpatterns = [

    path('archivo/', include(('file.urls', 'file'), namespace='archivo')),
    path('usuario/', include(('usuario.urls', 'usuario'), namespace='usuario'))

]
