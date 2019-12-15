# Generated by Django 2.2.6 on 2019-11-06 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LlamadasEntrantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_solicitante', models.CharField(max_length=20)),
                ('ident_fiscal', models.IntegerField()),
                ('nombre_destinatario', models.CharField(max_length=30)),
                ('direccion_des_mcia', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('telebox', models.CharField(max_length=30)),
                ('zona_transporte', models.CharField(max_length=30)),
                ('material', models.IntegerField()),
                ('texto_breve_material', models.CharField(max_length=30)),
                ('documento_ventas', models.IntegerField()),
                ('entrega', models.IntegerField()),
                ('num_pedido_cliente', models.CharField(max_length=15)),
                ('cantidad_pedido', models.CharField(max_length=15)),
                ('observaciones_inicial', models.CharField(max_length=255)),
                ('denom_articulos', models.CharField(max_length=30)),
                ('nombre_contacto', models.CharField(max_length=30)),
                ('resultado_llamada', models.CharField(max_length=30)),
                ('fecha_entrega_confirmada', models.CharField(max_length=30)),
                ('localidad', models.CharField(max_length=30)),
                ('barrio', models.CharField(max_length=30)),
                ('ruta', models.CharField(max_length=30)),
                ('hora_inicio', models.CharField(max_length=30)),
                ('hora_final', models.CharField(max_length=30)),
                ('observaciones_llamadas', models.CharField(max_length=255)),
                ('llamada_ead', models.CharField(max_length=255)),
                ('Operador', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]