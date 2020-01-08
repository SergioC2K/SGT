"""Formulario Modulo de Llamadas"""

# Django

from django import forms

# Modelos
from file.models.archivo import LlamadasEntrantes


class CargaLlamadas(forms.Form):
    leido = pd.read_excel(request.FILES['myfile'])
    llamadas = []
    for data in leido.T.to_dict().values():
        llamadas.append(LlamadasEntrantes(**data))
    pass