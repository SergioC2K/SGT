import datetime

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from tablib import Dataset
from file.models import LlamadasEntrantes
import pandas as pd
from django.views.generic import ListView, CreateView, UpdateView
from django.db.models import Q, Count

# Create your views here.
from usuario.models import Perfil
import time


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

hoy = datetime.date.today()
manana = hoy + datetime.timedelta(days=1)
dias_antes = hoy - datetime.timedelta(days=9)
horas_antes = hoy - datetime.timedelta(hours=12)


class ListarArchivo(ListView):
    model = LlamadasEntrantes
    template_name = 'archivo/listar_archivo.html'
    queryset = LlamadasEntrantes.objects.filter(created__range=(horas_antes, manana))
    context_object_name = 'llamadas_hoy'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        llamadas_hoy = self.queryset
        duplicadas = llamadas_hoy.values('entrega') \
            .annotate(repetidas=Count('entrega')) \
            .order_by() \
            .filter(repetidas__gte=2)

        data['doble_llamada'] = self.queryset. \
            filter(entrega__in=[repe['entrega'] for repe in duplicadas])

        data['usuario_conectado'] = Perfil.objects.filter(conexion__estado=True)

        # Llamadas seguimiento son las llamadas que han quedado pendiente o algun estado similar
        data['llamadas_seguimiento'] = LlamadasEntrantes.objects. \
            filter(
            Q(created__range=(dias_antes, horas_antes)),
            Q(entrega__in=self.queryset.values('entrega'))
        )
        return data


def registro_llamada(request):
    global response
    if request.is_ajax():
        data = {
            'is_taken': LlamadasEntrantes.objects.filter(created__range=(horas_antes, manana))
        }
        response = JsonResponse(data)
        response.status_code = 200
    return response


def repartir_llamada(request):

    if request.method == 'POST':
        pass
    return render(request, 'llamada/registro_llamada.html')