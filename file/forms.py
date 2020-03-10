"""Formulario Modulo de Llamadas"""
# Date
from datetime import datetime
import datetime as fechas
# Excel
import pandas as pd

# Django
from django import forms
from django.core.exceptions import ValidationError

# Modelos
from file.models import Estado, RegistroLlamada, Grabacion, Archivo


class SubirArchivo(forms.Form):
    """Formulario Subida de Llamadas"""

    archivo = forms.FileField()

    def clean_archivo(self):
        archivo = self.cleaned_data['archivo']
        nombre_existe = Archivo.objects.filter(nombre=archivo.name).exists()

        if len(archivo.name) >= 4 and archivo.name[-4:] == '.xlsx':
            raise forms.ValidationError('Ese tipo de archivo no se puede subir al sistema')

        if nombre_existe:
            raise forms.ValidationError('Este archivo ya fue cargado al sistema')

        return archivo

    def clean(self):
        data = super().clean()
        try:
            pd.read_excel(data['archivo'])
        except ImportError as I:
            raise forms.ValidationError('Ha ocurrido un problema con el archivo'%I)



class RealizarLlamada(forms.Form):
    """Formulario Validación y Realización de Llamada"""

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
# TODO
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
                                                                          'id': 'customFile',
                                                                          'required': False})
                                   )
    id_llamada = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'id_llamada',
        'name': 'id_llamada',

    }))

    def clean_fecha_entrega(self):
        """Verificar que la fecha de entrega ingresada sea mayor a la actual"""
        try:
            fecha = self.cleaned_data['fecha_entrega']
            ya = fechas.date.today()
            oelo = datetime.strptime(fecha, '%Y-%m-%d').date()
            if oelo > ya:
                return fecha
        except ValidationError as e:
            raise forms.ValidationError('Ingrese una fecha correcta!' % e)

    def clean(self):
        """Clean."""
        data = super().clean()
        return data

    def save(self):
        """Crear la llamada realizada por el operador."""
        data = self.cleaned_data
        if self.files:
            audio = data['id_grabacion']
            nombre = data['id_grabacion'].name
            grabacion = Grabacion(nombre=nombre, audio=audio)
            grabacion.save()
            llamada = RegistroLlamada.objects.get(id=data['id_llamada'])
            llamada.fecha_entrega = data['fecha_entrega']
            llamada.observaciones = data['observaciones']
            llamada.realizado = data['realizado']
            estado = Estado.objects.get(id=data['id_estado'])
            llamada.id_estado = estado
            llamada.id_grabacion = grabacion
            llamada.save()
        else:
            llamada = RegistroLlamada.objects.get(id=data['id_llamada'])
            llamada.fecha_entrega = data['fecha_entrega']
            llamada.observaciones = data['observaciones']
            llamada.realizado = data['realizado']
            estado = Estado.objects.get(id=data['id_estado'])
            llamada.id_estado = estado
            llamada.save()


class LlamadaModelo(forms.ModelForm):
    class Meta:
        model = RegistroLlamada
        fields = '__all__'
