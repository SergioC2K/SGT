from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from tablib import Dataset
from file.models.archivo import LlamadasEntrantes
import pandas as pd
from django.views.generic import ListView, CreateView, UpdateView


# Create your views here.
@login_required
def upload_excel(request):
    if request.method == 'POST':
        leido = pd.read_excel(request.FILES['myfile'])
        llamadas = []
        for data in leido.T.to_dict().values():
            llamadas.append(
                LlamadasEntrantes(
                    nombre_solicitante=data['Nombre solicitante'],
                    ident_fiscal=data['Ident.Fiscal Dest Mcia'],
                    nombre_destinatario=data['Nombre destinatario'],
                    direccion_des_mcia=data['Dirección Dest Mcia'],
                    telefono=data['Teléfono 1'],
                    telebox=data['Telebox'],
                    zona_transporte=data['Zona de transporte'],
                    material=data['Material'],
                    texto_breve_material=data['Texto breve material'],
                    documento_ventas=data['Documento de ventas'],
                    entrega=data['Entrega'],
                    num_pedido_cliente=data['Nº pedido cliente'],
                    cantidad_pedido=data['Cantidad de pedido'],
                    observaciones_inicial=data['Observaciones'],
                    denom_articulos=data['Denom.gr-artículos'],
                    localidad=data['localidad'],
                    barrio=data['barrio'],
                    ruta=data['ruta'],
                    hora_inicio=data['hora inicial'],
                    hora_final=data['hora final']
                ))

        LlamadasEntrantes.objects.bulk_create(llamadas)
    return render(request, 'archivo/fileimport.html')


def preview_excel(request):
    if request.method == 'POST':
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        data_final = imported_data.export('json')

    return render(request, 'archivo/fileimport.html')


class listar_archivo(ListView):
    model = LlamadasEntrantes
    template_name = 'archivo/listar_archivo.html'
