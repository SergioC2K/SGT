from django import forms
from .models import Estado, RegistroLlamada, LlamadasEntrantes
from django.contrib.auth.models import User

import django_filters


class filtro(django_filters.FilterSet):
    id_estado__nombre = django_filters.ModelMultipleChoiceFilter(
        queryset=Estado.objects.values_list('nombre', flat=True),
        widget=forms.Select(attrs={'class': 'form-control search-slt',
                                   'id': 'exampleFormControlSelect1'}))

    id_usuario__telefono_fijo = django_filters.ModelMultipleChoiceFilter(
        queryset=User.objects.values_list('username', flat=True),
        widget=forms.Select(attrs={'class': 'form-control search-slt',
                                   'id': 'exampleFormControlSelect1'}))

    id_usuario__fechaEntrega = django_filters.ModelMultipleChoiceFilter(
        queryset=RegistroLlamada.objects.values_list('fecha_entrega', flat=True),
        widget=forms.Select(attrs={'class': 'form-control search-slt',
                                   'id': 'exampleFormControlSelect1'}))

    class Meta:
        model = RegistroLlamada
        fields = ['id_estado']
