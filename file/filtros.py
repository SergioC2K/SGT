import django_filters
from django import forms

from usuario.models import Perfil
from .models import Estado, RegistroLlamada


class filtro(django_filters.FilterSet):
    id_estado__nombre = django_filters.ModelMultipleChoiceFilter(
        queryset=Estado.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control search-slt',
                                           'id': 'exampleFormControlSelect1',

                                           }))

    id_usuario__telefono_fijo = django_filters.ModelMultipleChoiceFilter(
        queryset=Perfil.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control search-slt',
                                   'id': 'exampleFormControlSelect1'}))

    id_usuario__fechaEntrega = django_filters.ModelMultipleChoiceFilter(
        queryset=RegistroLlamada.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control search-slt',
                                   'id': 'exampleFormControlSelect1'}))

    class Meta:
        model = RegistroLlamada
        fields = ['id_estado']
