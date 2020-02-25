"""Formulario Modulo de Llamadas"""
# Date
import datetime

# Django

from django import forms
from django.core.exceptions import ValidationError

from SGT import settings
from file.models import Estado, RegistroLlamada, Grabacion
import os
from mutagen.mp3 import MP3, HeaderNotFoundError, InvalidMPEGHeader

from django.conf import settings


class RealizarLlamada(forms.Form):
    nombre_contesta = forms.CharField(
        max_length=45,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'alm_soli',
            'name': 'alm_soli',
            'placeholder': 'Nombre Contesta'
        })
    )
    fecha_entrega = forms.CharField(
        max_length=10,
        min_length=10,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'datepicker',
            'placeholder': 'Fecha de Entrega'
        })
    )
    observaciones = forms.CharField(widget=forms.Textarea)
    realizado = forms.BooleanField(initial=True, widget=forms.HiddenInput())
    id_estado = forms.ChoiceField(
        choices=Estado.ESTADOS,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'resultado_llamada',
            'name': 'resultado_llamada',
            'placeholder': 'Resultado de la llamada'
        })

    )
    id_grabacion = forms.FileField()
    id_llamada = forms.IntegerField()

    def clean_fecha_entrega(self):
        """Verificar que la fecha de entrega ingresada sea mayor a la actual"""
        try:
            fecha = self.cleaned_data['fecha_entrega']
            fechita = datetime.datetime.strptime(fecha, "%m/%d/%Y").date()
            ya = datetime.date.today()
            if fechita > ya:
                return fecha
        except ValidationError as e:
            raise forms.ValidationError('Ingrese una fecha correcta!'%e)

    def clean(self):
        """Clean."""
        data = super().clean()
        return data

    def save(self):
        """Crear la llamada realizada por el operador."""
        data = self.files['id_grabacion']
        nombre = self.files['id_grabacion'].name
        usuario = self.auto_id.pk
        estado = self.cleaned_data['id_estado']
        llamada = Grabacion(nombre=nombre, url=data)
        llamada.save()


class LlamadaModelo(forms.ModelForm):
    class Meta:
        model = RegistroLlamada
        fields = '__all__'