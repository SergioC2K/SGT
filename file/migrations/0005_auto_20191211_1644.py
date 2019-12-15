# Generated by Django 2.2.2 on 2019-12-11 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0004_auto_20191210_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='barrio',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='cantidad_pedido',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='denom_articulos',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='direccion_des_mcia',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='documento_ventas',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='entrega',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='hora_final',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='hora_inicio',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='ident_fiscal',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='localidad',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='material',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='nombre_destinatario',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='nombre_solicitante',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='num_pedido_cliente',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='ruta',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='telebox',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='telefono',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='texto_breve_material',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='llamadasentrantes',
            name='zona_transporte',
            field=models.CharField(max_length=50),
        ),
    ]