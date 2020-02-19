import datetime

from django.db import IntegrityError

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.http import JsonResponse
from django.shortcuts import render
from tablib import Dataset
from file.models import LlamadasEntrantes
import pandas as pd
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.db.models import Q, Count
from file.models import RegistroLlamada
from django.shortcuts import render, redirect
from file.models import LlamadasEntrantes, Archivo
from usuario.models import Perfil, User

# Create your views here.
from usuario.models import Perfil
import time


@login_required
def upload_excel(request):
    if request.method == 'POST':
        nombre = request.FILES['myfile']
        try:
            crear = Archivo.objects.create(nombre=nombre)

            crear.save()
        except IntegrityError as e:

            return render(request, 'archivo/fileimport.html', context={'errors': e})

        leido = pd.read_excel(nombre)
        llamadas = []
        crear = Archivo.objects.create(nombre=nombre)
        crear.save()
        for data in leido.T.to_dict().values():
            llamadas.append(
                LlamadasEntrantes(
                    id_archivo=Archivo.objects.last(),
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


class ListarArchivo(ListView):
    hoy = datetime.date.today()
    manana = hoy + datetime.timedelta(days=1)
    dias_antes = hoy - datetime.timedelta(days=9)
    horas_antes = hoy - datetime.timedelta(hours=12)

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
            Q(created__range=(self.dias_antes, self.horas_antes)),
            Q(entrega__in=self.queryset.values('entrega'))
        )
        return data


def registro_llamada(request):
    return render(request, 'llamada/registro_llamada.html')


class buzon(ListView):
    model = LlamadasEntrantes
    template_name = 'llamada/Buzon.html'


class entregar(ListView):
    template_name = 'llamada/entregar.html'
    model = Perfil

    def get(self, request, *args, **kwargs):
        name = request.GET['name']
        perfiles = Perfil.objects.get(usuario__first_name=name)
        data = serializers.serialize('json', perfiles, fields=('first_name', 'is_superuser'))
        return HttpResponse(data, content_type='application/json')


def repartir(request):
    #  Traemos todos los operadores activos para repartirles las llamdas
    operadores = Perfil.objects.all()

    #  Consultamos el ultimo archivo ingresado
    archivo = Archivo.objects.last()

    #  Se consultan las ultimas llamadas ingresadas de acuerdo a el archivo
    llamadas = LlamadasEntrantes.objects.filter(id_archivo=archivo).exclude(estado=True)
    if operadores and llamadas:
        contexto = {'operadores': operadores, 'llamadas': llamadas}
        return render(request, 'archivo/repartir.html', contexto)

    return render(request, 'archivo/repartir.html', {'error': 'No hay archivos para repartir'})


def enviarLlamadas(request):
    if request.method == 'POST':

        #  Capturamos los valores ingresados en la reparticion de las llamadas con un array
        valor = request.POST.getlist('valor[]')
        operador = request.POST.getlist('usuario[]')

        #  Miramos cual es la cantidad que tienen el array anterior
        dato = len(valor)
        contador = int(dato)

        #  Se consulta el ultimo archivo ingresado para traer las ultimas llamdadas registradas
        archivo = Archivo.objects.last()

        #  Segun la cantidad del array hacemos un for que recorra esa cantidad de datos
        for i in range(contador):
            #  Hacemos una consulta que nos traiga la cantidad de llamadas indicada en el array "valor"
            consulta = LlamadasEntrantes.objects.filter(id_archivo=archivo, estado=False).order_by('-pk')[
                       1:int(valor[i]) + 1]
            #  Recorremos la consulta anterior y la actualizamos segun el operador que indica el array "operador"
            for obj in consulta:
                usuario = User.objects.get(id=operador[i])
                obj.id_usuario = usuario.id
                obj.estado = True
                obj.save()

        #  Hacemos una consulta que nos traiga las ultimas llamdas ingresadas
        Registra = LlamadasEntrantes.objects.filter(id_archivo=archivo)
        for i in Registra:
            #  Ingresamos en la tabla "Registro llamada" el id de "Llamadas entrates"
            #  Esto se hace para poder conocer cuales son las llamadas que aun no se han realizado
            #  pero que si se han repartidor, Para despues poder hacer la validacion y mostrarselas a el operador
            creacion = RegistroLlamada.objects.create(id_llamada_id=int(i.id))
            creacion.save()

        return redirect('archivo:import')


def ver_Llamadas(request):
    registro = RegistroLlamada.objects.filter(realizado=False)
    diccionario = {'array': registro}

    return render(request, 'llamada/llegadas.html', diccionario)


class archivoLlamadas(ListView):
    model = Archivo
    template_name = 'archivo/eliminar_archivo.html'


def eliminarArchivo(request):
    archivo = request.GET.get('id', None)
    consulta = LlamadasEntrantes.objects.filter(id_archivo=archivo)
    auxiliar = 0
    for i in consulta:
        if i.estado:
            auxiliar = auxiliar + 1

    if auxiliar == 0:
        Archivo.objects.get(id=archivo).delete()
        data = {
            'deleted': True
        }
    else:
        data = {
            'deleted': False
        }

    return JsonResponse(data)


def reportes(request):
    return render(request, 'llamada/reportes.html')
