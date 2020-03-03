from django import forms
from .models import Estado, RegistroLlamada, LlamadasEntrantes
from django.contrib.auth.models import User

import django_filters


class filtro(django_filters.FilterSet):
    id_estado__nombre = django_filters.ModelMultipleChoiceFilter(queryset=Estado.objects.all(),
                                                                 widget=forms.Select(attrs={'class': 'form-control'}))
    id_usuario__telefono_fijo = django_filters.CharFilter()

    class Meta:
        model = Estado
        fields = ['nombre']
