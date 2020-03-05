# Generated by Django 2.2.2 on 2020-03-04 19:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conectado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha-Hora en que se creo.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora en que se modificó el objeto por última vez.', verbose_name='modified at')),
                ('estado', models.BooleanField(choices=[(True, 'Conectado'), (False, 'No Conectado')], default=False)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha-Hora en que se creo.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Fecha y hora en que se modificó el objeto por última vez.', verbose_name='modified at')),
                ('cedula', models.PositiveIntegerField(default='0')),
                ('telefono_fijo', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='El numero de telefono debe tener el siguiente formato 1234567890, sin comas ni signos de puntuacion. maximo hasta 10 caracteres. mimnimo 7 caracteres', regex='^[1-9]\\d{6,9}$')])),
                ('celular', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='El numero de telefono debe tener el siguiente formato 1234567890, sin comas ni signos de puntuacion. maximo hasta 10 caracteres. mimnimo 7 caracteres', regex='^[1-9]\\d{6,9}$')])),
                ('celular_telemercadeo', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='El numero de telefono debe tener el siguiente formato 1234567890, sin comas ni signos de puntuacion. maximo hasta 10 caracteres. mimnimo 7 caracteres', regex='^[1-9]\\d{6,9}$')])),
                ('foto', models.ImageField(blank=True, null=True, upload_to='media/pictures')),
                ('conexion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='usuario.Conectado')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
