from django import forms
from .models import Estado, RegistroLlamada, LlamadasEntrantes
from django.contrib.auth.models import User

import django_filters


class RegistroLlamadaFilter(django_filters.FilterSet):
    id_estado = django_filters.ModelMultipleChoiceFilter(
        queryset=Estado.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    id_usuario__telefono_fijo = django_filters.CharFilter()

    class Meta:
        model = RegistroLlamada
        fields = ['nombre_contesta', 'fecha_entrega', 'id_estado']
