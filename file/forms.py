"""Formulario Modulo de Llamadas"""

# Django

from django import forms
# Date
import datetime

# Django

from django import forms
from django.core.exceptions import ValidationError

from SGT import settings
from file.models import Estado, RegistroLlamada, Grabacion


class RealizarLlamada(forms.Form):
    NOCON = 1
    INFO_EN = 2
    DATERR = 3
    CLEAL = 4
    ZNCUB = 5
    CLAPLE = 6
    CLINOSOL = 7
    ALCOMPE = 8
    CLDES = 9
    ESTADOS = [
        (NOCON, 'No contesta'),
        (INFO_EN, 'Informacion de la entrega'),
        (DATERR, 'Datos Errados'),
        (CLEAL, 'Cliente pide entrega en almacen'),
        (ZNCUB, 'Zona no cubierta TCL'),
        (CLAPLE, 'Cliente aplaza entrega'),
        (CLINOSOL, 'Cliente no sabe de la solicitud'),
        (ALCOMPE, 'Almacen se compromete con entrega'),
        (CLDES, 'Cliente Desiste de la compra'),
    ]

    nombre_contesta = forms.CharField(
        max_length=45,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'nombre_contesta',
            'name': 'nombre_contesta',
            'placeholder': 'Nombre Contesta'
        })
    )
    fecha_entrega = forms.CharField(
        max_length=10,
        min_length=10,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'fecha_entrega',
            'name': 'fecha_entrega',
            'width': '250',
            'placeholder': 'Fecha de Entrega'
        })
    )
    observaciones = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                                 'id': 'observaciones',
                                                                 'rows': '2'
                                                                 })
                                    )
    realizado = forms.BooleanField(initial=True, widget=forms.HiddenInput())
    id_estado = forms.ChoiceField(
        choices=ESTADOS,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'resultado_llamada',
            'name': 'resultado_llamada',
            'placeholder': 'Resultado de la llamada'
        })

    )
    id_grabacion = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input',
                                                                          'id': 'customFile'})
                                   )
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
            raise forms.ValidationError('Ingrese una fecha correcta!' % e)

    def clean(self):
        """Clean."""
        data = super().clean()
        return data

    def save(self):
        """Crear la llamada realizada por el operador."""
        if self.files:
            audio = self.files['id_grabacion']
            nombre = self.files['id_grabacion'].name
            grabacion = Grabacion(nombre=nombre, audio=audio)
            grabacion.save()
            llamada = RegistroLlamada.objects.get(id=self.cleaned_data['id_llamada'])
            llamada.fecha_entrega = self.cleaned_data['fecha_entrega']
            llamada.observaciones = self.cleaned_data['observaciones']
            llamada.realizado = self.cleaned_data['realizado']
            llamada.id_llamada = self.cleaned_data['id_llamada']
            llamada.id_estado = self.cleaned_data['id_estado']
            llamada.id_grabacion = grabacion
            llamada.save()
        else:
            llamada = RegistroLlamada.objects.get(id=self.cleaned_data['id_llamada'])
            llamada.fecha_entrega = self.cleaned_data['fecha_entrega']
            llamada.observaciones = self.cleaned_data['observaciones']
            llamada.realizado = self.cleaned_data['realizado']
            llamada.id_llamada = self.cleaned_data['id_llamada']
            llamada.id_estado = self.cleaned_data['id_estado']
            llamada.save()


class LlamadaModelo(forms.ModelForm):
    class Meta:
        model = RegistroLlamada
        fields = '__all__'
