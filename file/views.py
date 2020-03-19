# Date
import datetime
from datetime import date
# Excel
import pandas as pd
# Django
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView
from django.db.models import Q, Count
from django.db import IntegrityError
# Modelos
from file.forms import RealizarLlamada
from file.models import RegistroLlamada
from file.models import LlamadasEntrantes, Archivo, Estado
from usuario.models import Perfil

# Filtros
from .filters import RegistroLlamadaFilter

hoy = datetime.date.today()
manana = hoy + datetime.timedelta(days=1)
dias_antes = hoy - datetime.timedelta(days=9)
horas_antes = hoy - datetime.timedelta(hours=12)


@login_required
def upload_excel(request):
    if request.method == 'POST':
        nombre = request.FILES['myfile']
        leido = pd.read_excel(nombre)
        llamadas = []
        try:
            archivo = Archivo.objects.create(nombre=nombre)
            archivo.save()
        except IntegrityError as e:
            return render(request, 'archivo/fileimport.html', context={"message": e})

        for data in leido.T.to_dict().values():
            llamadas.append(
                LlamadasEntrantes(
                    archivo=archivo,
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
                )
            )
        LlamadasEntrantes.objects.bulk_create(llamadas)
    return render(request, 'archivo/fileimport.html')


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
        #  Capturamos los valores ingresados en la reparticion de las llamadas con un array
        valor = request.POST.getlist('valor[]')
        operador = request.POST.getlist('usuario[]')

        #  Segun la cantidad del array hacemos un for que recorra esa cantidad de datos
        for i in range(len(valor)):
            #  Hacemos una consulta que nos traiga la cantidad de llamadas indicada en el array "valor"
            llamadas = LlamadasEntrantes.objects.filter(created__range=(horas_antes, manana)).exclude(estado=True) \
                [:int(valor[i])]
            #  Recorremos la consulta anterior y la actualizamos segun el operador que indica el array "operador"
            for llam in llamadas:
                registro = RegistroLlamada(id_llamada=llam, id_usuario_id=operador[i])
                registro.save()
                llam.estado = True
                llam.save()
        return redirect('archivo:import')


def ver_Llamadas(request):
    usuario = request.user.pk
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


def traer(request):
    persona = request.GET.get('id', None)
    consulta = RegistroLlamada.objects.get(id_llamada_id=persona)

    data = {'nombre': consulta.id_llamada.nombre_destinatario,
            'ruta': consulta.id_llamada.ruta,
            'telefono': consulta.id_llamada.telefono,
            'direccion_des_mcia': consulta.id_llamada.direccion_des_mcia,
            'alm_soli': consulta.id_llamada.nombre_solicitante,
            'localidad': consulta.id_llamada.localidad}

    return JsonResponse(data)


class ListFile(ListView):
    model = Perfil
    template_name = 'llamada/exportar.html'


def realizar_llamada(request, number):
    global llamadas, data
    if request.method == 'POST':
        llamada = RegistroLlamada.objects.get(id=number)
        form = RealizarLlamada(request.POST, request.FILES, request.user)
        if form.is_valid():
            form.save()
            data = {
                'form': form,
                'aprobado': 'ok',
                'llamada': llamada,
                'errores': form.errors
            }
            return render(request, template_name='llamada/Buzon.html', context=data)
        else:
            data = {
                'form': form.errors,
                'No_Aprobado': 'NO',
                'llamada': llamada
            }
            return render(request, template_name='llamada/Buzon.html', context=data)
    else:
        form = RealizarLlamada()
        llamada = RegistroLlamada.objects.get(id=number)
        data = {
            'form': form,
            'llamada': llamada
        }
    return render(request, template_name='llamada/Buzon.html', context=data)


def pruebas_llamadas(request):
    user_list = RegistroLlamada.objects.all()
    user_filter = RegistroLlamadaFilter(request.GET, queryset=user_list)
    return render(request, 'prueba.html', {'filter': user_filter})


def traer(request):
    persona = request.GET.get('id', None)
    consulta = RegistroLlamada.objects.get(id_llamada_id=persona)
    data = {'nombre': consulta.id_llamada.nombre_destinatario, 'ruta': consulta.id_llamada.ruta,
            'telefono': consulta.id_llamada.telefono,
            'direccion_des_mcia': consulta.id_llamada.direccion_des_mcia,
            'alm_soli': consulta.id_llamada.nombre_solicitante,
            'localidad': consulta.id_llamada.localidad}
    return JsonResponse(data)


def search(request):
    user_list = RegistroLlamada.objects.all()
    user_filter = RegistroLlamadaFilter(request.GET, queryset=user_list)
    return render(request, 'llamada/exportar.html', {'filter': user_filter})


#  Este metodo solo es para que me retorne al template
def reporte_llamada(request):
    return render(request, 'reportes/reporte_llamada.html')


#  Este metodo me va retornar las estadisticas de los estados
#  Segun la fecha indicada por el usuario
def traer_reporte_llamada(request):
    # La variable dia me trae el valor de la fecha a consultar
    dia = request.GET.get('valor', None)
    fecha = date.today()
    valor = int(dia)

    if valor == 0:
        no_contesta = RegistroLlamada.objects.filter(id_estado__nombre='No contesta').count()
        exito = RegistroLlamada.objects.filter(id_estado__nombre='Exitoso').count()
        data = {
            'no_contesta': no_contesta,
            'exito': exito
        }

    elif valor == 1:
        ayer = fecha.day - 1
        exito = RegistroLlamada.objects.filter(modified__day=ayer, id_estado__nombre='Exitoso').count()
        no_contesta = RegistroLlamada.objects.filter(modified__day=ayer, id_estado__nombre='No contesta').count()
        data = {
            'no_contesta': no_contesta,
            'exito': exito
        }

    elif valor == 2:
        hoy = datetime.datetime.utcnow()
        semana = hoy - datetime.timedelta(days=7)
        exito = RegistroLlamada.objects.filter(id_estado__nombre='Exitoso', modified__range=[semana, hoy]).count()
        no_contesta = RegistroLlamada.objects.filter(id_estado__nombre='No contesta',
                                                     modified__range=[semana, hoy]).count()

        data = {
            'no_contesta': no_contesta,
            'exito': exito
        }

    elif valor == 3:
        hoy = datetime.datetime.utcnow()
        mes = hoy - datetime.timedelta(days=30)
        exito = RegistroLlamada.objects.filter(id_estado__nombre='Exitoso', modified__range=[mes, hoy]).count()
        no_contesta = RegistroLlamada.objects.filter(id_estado__nombre='No contesta',
                                                     modified__range=[mes, hoy]).count()

        data = {
            'no_contesta': no_contesta,
            'exito': exito
        }

    return JsonResponse(data=data)


#  Este metodo me retorna a la vista indicada
def reporte_usuario(request):
    usuario = Perfil.objects.all()

    data = {
        'usuario': usuario
    }
    return render(request, 'reportes/reporte_usuario.html', data)


def traer_reporte_usuario(request):
    dia = request.GET.get('valor', None)
    usuario = request.GET.get('usuario', None)
    fecha = date.today()
    valor = int(dia)
    id = int(usuario)

    if valor == 0:
        exito = RegistroLlamada.objects.filter(id_usuario=id, id_estado__nombre='Exitoso').count()
        nombre = Perfil.objects.get(usuario_id=id)

        data = {
            'exito': exito,
            'nombre': nombre.usuario.first_name
        }

    elif valor == 1:
        ayer = fecha.day - 1
        exito = RegistroLlamada.objects.filter(modified__day=ayer, id_usuario=id, id_estado__nombre='Exitoso').count()
        no_contesta = RegistroLlamada.objects.filter(modified__day=ayer, id_usuario=id, id_estado=2).count()
        nombre = Perfil.objects.get(usuario_id=id)

        data = {
            'exito': exito,
            'no_contesta': no_contesta,
            'nombre': nombre.usuario.first_name
        }

    elif valor == 2:
        hoy = datetime.datetime.utcnow()
        semana = hoy - datetime.timedelta(days=7)
        exito = RegistroLlamada.objects.filter(modified__range=[semana, hoy],
                                               id_usuario=id,
                                               id_estado__nombre='Exitoso').count()
        no_contesta = RegistroLlamada.objects.filter(modified__range=[semana, hoy],
                                                     id_usuario=id,
                                                     id_estado__nombre='No contesta').count()

        nombre = Perfil.objects.get(usuario_id=id)

        data = {
            'no_contesta': no_contesta,
            'exito': exito,
            'nombre': nombre.usuario.first_name
        }

    elif valor == 3:
        hoy = datetime.datetime.utcnow()
        mes = hoy - datetime.timedelta(days=30)
        exito = RegistroLlamada.objects.filter(id_estado__nombre='Exitoso', id_usuario=id,
                                               modified__range=[mes, hoy]).count()

        no_contesta = RegistroLlamada.objects.filter(id_estado__nombre='No contesta', id_usuario=id,
                                                     modified__range=[mes, hoy]).count()

        nombre = Perfil.objects.get(usuario_id=id)

        data = {
            'no_contesta': no_contesta,
            'exito': exito,
            'nombre': nombre.usuario.first_name
        }

    return JsonResponse(data=data)


#  Esta es el metodo donde el coordinador va exportar para enviar aceb
def reporte_general(request):
    hoy = datetime.datetime.utcnow()
    hora = hoy - datetime.timedelta(hours=24)
    registradas = RegistroLlamada.objects.filter(modified__range=[hora, hoy])
    data = {
        'dia': 'Llamadas del dia de hoy',
        'registro': registradas
    }
    return render(request, 'reportes/reporte_general.html', data)


def trer_reporte_general(request):
    diccionario = {}
    respuesta = request.POST['respuesta']
    valor = int(respuesta)

    if valor == 0:
        consulta = RegistroLlamada.objects.all()
        if consulta:
            diccionario = {'registro': consulta}
        else:
            diccionario = {'error': 'error'}

    elif valor == 1:
        hoy = datetime.datetime.utcnow()
        horas = hoy - datetime.timedelta(hours=36)
        consulta = RegistroLlamada.objects.filter(modified__range=[hoy, horas])

        if consulta:
            diccionario = {'registro': consulta}
        else:
            diccionario = {'error': 'error'}

    elif valor == 2:
        hoy = datetime.datetime.utcnow()
        semana = hoy - datetime.timedelta(days=7)
        consulta = RegistroLlamada.objects.filter(modified__range=[semana, hoy])

        if consulta:
            diccionario = {'registro': consulta}
        else:
            diccionario = {'error': 'error'}

    elif valor == 3:
        hoy = datetime.datetime.utcnow()
        mes = hoy - datetime.timedelta(days=30)
        consulta = RegistroLlamada.objects.filter(modified__range=[mes, hoy])

        if consulta:
            diccionario = {'registro': consulta}
        else:
            diccionario = {'error': 'error'}

    elif valor == 4:
        archivo = Archivo.objects.last()
        registradas = RegistroLlamada.objects.filter(id_llamada__archivo_id=archivo)
        diccionario = {
            'registro': registradas
        }

    return render(request, template_name='reportes/reporte_general.html', context=diccionario)
