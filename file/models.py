from django.db import models


# Create your models here.
class LlamadasEntrantes(models.Model):

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
