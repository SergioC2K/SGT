# Generated by Django 2.2.2 on 2019-12-10 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_auto_20191106_0334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='llamadasentrantes',
            name='Operador',
        ),
        migrations.RemoveField(
            model_name='llamadasentrantes',
            name='fecha_entrega_confirmada',
        ),
        migrations.RemoveField(
            model_name='llamadasentrantes',
            name='llamada_ead',
        ),
        migrations.RemoveField(
            model_name='llamadasentrantes',
            name='nombre_contacto',
        ),
        migrations.RemoveField(
            model_name='llamadasentrantes',
            name='observaciones_llamadas',
        ),
        migrations.RemoveField(
            model_name='llamadasentrantes',
            name='resultado_llamada',
        ),
    ]