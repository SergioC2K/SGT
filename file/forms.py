"""Formulario Modulo de Llamadas"""

# Django

from django import forms



class RealizarLlamada(forms.Form):

    nombre_contesta = forms.CharField(max_length=45)
    fecha_entrega = forms.DateField()
    observaciones = forms.CharField(widget=forms.Textarea)
    id_estado_id = 'oe'
    pass