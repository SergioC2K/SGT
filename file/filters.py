from django import forms
from .models import Estado, RegistroLlamada, LlamadasEntrantes, Grabacion
from django.contrib.auth.models import User

import django_filters


class RegistroLlamadaFilter(django_filters.FilterSet):
    id_estado = django_filters.ModelMultipleChoiceFilter(queryset=Estado.objects.all(),widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-control'
        })
    )

    id_usuario__telefono_fijo = django_filters.CharFilter()

    class Meta:
        model = RegistroLlamada
        fields = ['nombre_contesta', 'fecha_entrega', 'id_estado', 'id_grabacion']
