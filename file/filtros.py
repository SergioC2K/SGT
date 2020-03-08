import django_filters
from django import forms

from usuario.models import Perfil
from .models import Estado, RegistroLlamada


class filtro(django_filters.FilterSet):
    id_estado = django_filters.ModelMultipleChoiceFilter(queryset=Estado.objects.all(),
                                                         widget=forms.CheckboxSelectMultiple)
    id_usuario = django_filters.ModelMultipleChoiceFilter(queryset=Perfil.objects.all(),
                                                          widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = RegistroLlamada
        fields = ['id_estado', 'id_usuario']
