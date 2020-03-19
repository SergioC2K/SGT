# Date
import datetime
# Excel
import pandas as pd
# Django
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, FormView
from django.db.models import Q, Count
from django.db import IntegrityError
# Modelos
from file.forms import RealizarLlamada, EstadoForm
from file.models import RegistroLlamada
from file.models import LlamadasEntrantes, Archivo, Estado
from usuario.models import Perfil
from file.forms import SubirArchivoForm

# Filtros
from .filters import RegistroLlamadaFilter

hoy = datetime.date.today()
manana = hoy + datetime.timedelta(days=1)
dias_antes = hoy - datetime.timedelta(days=9)
horas_antes = hoy - datetime.timedelta(hours=12)


@login_required
def upload_excel(request):
    if request.method == 'POST':
        form = SubirArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Las llamadas han sido cargadas al sistema')
        else:
            return render(request, 'archivo/fileimport.html', context={'form': form})
    else:
        form = SubirArchivoForm()

    return render(request, 'archivo/fileimport.html', context={'form': form})


superuser_required = user_passes_test(lambda u: u.is_staff, login_url=('usuario:perfil'))


@method_decorator(superuser_required, name='dispatch')
class ListarArchivo(ListView):
    model = LlamadasEntrantes
    template_name = 'archivo/listar_archivo.html'
    queryset = LlamadasEntrantes.objects.filter(created__range=(horas_antes, manana)).exclude(estado=True)
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
        ).exclude(estado=True)
        return data


def registro_llamada(request):
    global response, llamadas, calls, qs, qsssss
    if request.is_ajax():
        operador = request.GET['operador']
        llamadas = request.GET.getlist('llamadas[]')
        for i in range(len(llamadas)):
            registro_llamadas = RegistroLlamada(id_llamada_id=llamadas[i], id_usuario_id=operador)
            registro_llamadas.save()
            llamada_repartida = LlamadasEntrantes.objects.get(id=llamadas[i])
            llamada_repartida.estado = True
            llamada_repartida.save()
        devolver_llamadas = LlamadasEntrantes.objects.filter(created__range=(horas_antes, manana)) \
            .exclude(estado=True)
        qsssss = serializers.serialize('json', devolver_llamadas, fields=('pk', 'entrega'))
    return HttpResponse(qsssss, content_type='application/json')


def repartir(request):
    #  Traemos todos los operadores activos para repartirles las llamdas
    operadores = Perfil.objects.all()

    #  Consultamos el ultimo archivo ingresado
    archivo = Archivo.objects.last()

    #  Se consultan las ultimas llamadas ingresadas de acuerdo a el archivo
    llamadas = LlamadasEntrantes.objects.filter(archivo=archivo).exclude(estado=True)
    if operadores and llamadas:
        contexto = {'operadores': operadores, 'llamadas': llamadas}
        return render(request, 'archivo/repartir.html', contexto)

    return render(request, 'archivo/repartir.html', {'error': 'No hay archivos para repartir'})

@method_decorator(superuser_required, name='dispatch')
class entregar(ListView):
    template_name = 'llamada/entregar.html'
    model = Perfil

    def get(self, request, *args, **kwargs):
        name = request.GET['name']
        perfiles = Perfil.objects.get(usuario__first_name=name)
        data = serializers.serialize('json', perfiles, fields=('first_name', 'is_superuser'))
        return HttpResponse(data, content_type='application/json')


def enviarLlamadas(request):
    if request.method == 'POST':
        valor = request.POST.getlist('valor[]')
        operador = request.POST.getlist('usuario[]')

        for i in range(len(valor)):
            llamadas = LlamadasEntrantes.objects.filter(created__range=(horas_antes, manana)).exclude(estado=True) \
                [:int(valor[i])]
            for llam in llamadas:
                registro = RegistroLlamada(id_llamada=llam, id_usuario_id=operador[i])
                registro.save()
                llam.estado = True
                llam.save()
        return redirect('archivo:import')


def ver_Llamadas(request):
    usuario = request.user.perfil.pk
    estados = Estado.objects.all()
    registro = RegistroLlamada.objects.filter(id_usuario_id=usuario)
    data = {
        'diccionario': registro,
        'estados': estados
    }
    return render(request, 'llamada/Buzon.html', context=data)


@method_decorator(superuser_required, name='dispatch')
class archivoLlamadas(ListView):
    model = Archivo
    template_name = 'archivo/eliminar_archivo.html'


def eliminarArchivo(request):
    archivo = request.GET.get('id', None)
    consulta = LlamadasEntrantes.objects.filter(archivo=archivo)
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


class ListFile(ListView):
    model = Perfil
    template_name = 'llamada/exportar.html'


def realizar_llamada(request):
    global data
    usuario = request.user
    if request.method == 'POST':
        form = RealizarLlamada(request.POST, request.FILES, request.user)
        if form.is_valid():
            form.save()
            data = {
                'form': form,
                'aprobado': 'ok',
                'errores': form.errors
            }
            return render(request, template_name='llamada/Buzon.html', context=data)
        else:
            llamada = RegistroLlamada.objects.filter(id_usuario_id=usuario.perfil.pk)
            data = {
                'form': form.errors,
                'No_Aprobado': 'NO',
                'llamada': llamada
            }
            return render(request, template_name='llamada/Buzon.html', context=data)
    else:
        form = RealizarLlamada()
        estados = Estado.objects.all()
        llamada = RegistroLlamada.objects.filter(id_usuario_id=usuario.perfil.pk)
        data = {
            'form': form,
            'llamadas': llamada,
            'estados': estados
        }
    return render(request, template_name='llamada/Buzon.html', context=data)


def pruebas_llamadas(request):
    user_list = RegistroLlamada.objects.all()
    user_filter = RegistroLlamadaFilter(request.GET, queryset=user_list)
    return render(request, 'prueba.html', {'filter': user_filter})


def traer(request):
    llamada = int(request.GET.get('id', None))
    consulta = RegistroLlamada.objects.get(pk=llamada)
    oelooo = consulta.pk
    datos = {
        'id_llamada': consulta.pk,
        'nombre': consulta.id_llamada.nombre_destinatario,
        'ruta': consulta.id_llamada.ruta,
        'telefono': consulta.id_llamada.telefono,
        'direccion_des_mcia': consulta.id_llamada.direccion_des_mcia,
        'alm_soli': consulta.id_llamada.nombre_solicitante,
        'localidad': consulta.id_llamada.localidad
    }
    return JsonResponse(datos)


def search(request):
    user_list = RegistroLlamada.objects.all()
    user_filter = RegistroLlamadaFilter(request.GET, queryset=user_list)
    return render(request, 'llamada/exportar.html', {'filter': user_filter})


class CrearEstado(ListView, FormView):
    model = Estado
    form_class = EstadoForm
    template_name = 'llamada/estados.html'



