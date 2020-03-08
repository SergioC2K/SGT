# Models
from .models import RegistroLlamada
# Filtros
import django_filters


class RegistroLlamadaFilter(django_filters.FilterSet):

    class Meta:
        model = RegistroLlamada
        fields = ('nombre_contesta', 'id_estado__nombre')