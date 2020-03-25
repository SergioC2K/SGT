from django.contrib.auth.models import User
from django.db import models
from usuario.models import Perfil
from utils.models import BaseModel
from utils.models import BaseModel


class Archivo(BaseModel, models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class LlamadasEntrantes(BaseModel, models.Model):
    archivo = models.ForeignKey('Archivo', on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)

    nombre_solicitante = models.CharField(max_length=50)
    ident_fiscal = models.CharField(max_length=50)

    nombre_destinatario = models.CharField(max_length=50)
    direccion_des_mcia = models.CharField(max_length=50)

    telefono = models.CharField(max_length=50)
    telebox = models.CharField(max_length=50)

    zona_transporte = models.CharField(max_length=50)
    material = models.CharField(max_length=50)

    texto_breve_material = models.CharField(max_length=50)
    documento_ventas = models.CharField(max_length=50)

    entrega = models.CharField(max_length=50)
    num_pedido_cliente = models.CharField(max_length=50)

    cantidad_pedido = models.CharField(max_length=50)
    observaciones_inicial = models.CharField(max_length=255)

    denom_articulos = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)

    barrio = models.CharField(max_length=50)
    ruta = models.CharField(max_length=50)

    hora_inicio = models.CharField(max_length=50)
    hora_final = models.CharField(max_length=50)

    def __str__(self):
        return self.pk


class Grabacion(BaseModel, models.Model):
    # Url de donde va quedar almacenada la grabacion

    nombre = models.CharField(max_length=45)
    audio = models.FileField(upload_to='audio/mp3')

    def __str__(self):
        return self.nombre


class Estado(BaseModel, models.Model):
    nombre = models.CharField(max_length=35)

    def __str__(self):
        return self.nombre


class RegistroLlamada(BaseModel, models.Model):
    nombre_contesta = models.CharField(max_length=45, blank=False, null=True)
    fecha_entrega = models.DateField(null=True, blank=False)
    observaciones = models.TextField(null=True, blank=True)
    realizado = models.BooleanField(default=False, null=True)
    id_llamada = models.ForeignKey(LlamadasEntrantes, on_delete=models.PROTECT)
    id_usuario = models.ForeignKey(Perfil, null=True, on_delete=models.PROTECT)
    precio = models.PositiveSmallIntegerField(max_length=510)
    id_estado = models.ForeignKey('Estado', null=True, blank=False, on_delete=models.PROTECT)
    id_grabacion = models.ForeignKey('Grabacion', null=True, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)
