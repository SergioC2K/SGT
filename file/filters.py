import django_filters
from .models import RegistroLlamada
from usuario.models import Perfil


class RegistroLlamadaFilter(django_filters.FilterSet):
    id_usuario__telefono_fijo = django_filters.CharFilter()
    class Meta:
        model = RegistroLlamada
        fields = ['nombre_contesta', 'fecha_entrega']
