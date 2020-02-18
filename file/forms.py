"""Formulario Modulo de Llamadas"""

# Django

from django import forms



class RealizarLlamada(forms.Form):

    nombre_contesta = forms.CharField(max_length=45)
    pass