from django import forms
from .models import Estado, RegistroLlamada, LlamadasEntrantes
from usuario.models import Perfil
from django.contrib.auth.models import User

import django_filters


class filtro(django_filters.FilterSet):
    id_estado = django_filters.ModelMultipleChoiceFilter(queryset=Estado.objects.all(),
                                                         widget=forms.CheckboxSelectMultiple)
    id_usuario = django_filters.ModelMultipleChoiceFilter(queryset=Perfil.objects.all(),
                                                          widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = RegistroLlamada
        fields = ['id_estado', 'id_usuario']

